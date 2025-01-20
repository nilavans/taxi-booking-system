from Utils import generate_id
from Taxi import *
from BookTaxi import *
import threading
import time 

class TaxiManager:
    def __init__(self):
        self.taxis = self._initialise_taxi()
        self.bookings = {}
        self.lock = threading.Lock()

    # By default there will be atleast two taxi available.
    def _initialise_taxi(self):
        taxis = []
        for i in range(2):
            taxi_id = generate_id('TX')
            taxis.append(Taxi(taxi_id))
        return taxis
    
    def find_nearest_available_taxi(self, pickup_point, routes):
        available_taxis = [taxi for taxi in self.taxis if taxi.status == 'free']

        if not available_taxis:
            return None
        
        nearest_taxi = None
        min_distance = float('inf')

        for taxi in available_taxis:
            taxi_distance = abs(routes.index(pickup_point) - routes.index(taxi.station))
            if taxi_distance < min_distance:
                min_distance = taxi_distance
                nearest_taxi = taxi
            return nearest_taxi

    def taxi_allocate(self, pickup_point, routes):
        # Check if any taxis are available at station A.
        available_taxi_at_starting_point = [taxi for taxi in self.taxis if taxi.station == 'A' and taxi.status == 'free']
        if available_taxi_at_starting_point:
            taxi_to_allocate = min(available_taxi_at_starting_point, key=lambda taxi: taxi.earnings)
            taxi_to_allocate.status = 'occupied'
            print(f"Taxi {taxi_to_allocate.taxi_id} is allocated.")
            return taxi_to_allocate
        
        # If any taxi available at pickup point allocate the one with low earnings.
        available_taxi_at_pickup_point = [taxi for taxi in self.taxis if taxi.station == pickup_point and taxi.status == 'free']
        if available_taxi_at_pickup_point:
            taxi_to_allocate = min(available_taxi_at_starting_point, key=lambda taxi: taxi.earnings)
            taxi_to_allocate.status = 'occupied'
            print(f"Taxi {taxi_to_allocate.taxi_id} is allocated.")
            return taxi_to_allocate
        
        # If no taxi at station A and pickup point, then look for nearest available one.
        nearest_taxi = self.find_nearest_available_taxi(pickup_point, routes)
        if nearest_taxi:
            nearest_taxi.status = 'occupied'
            print(f"Taxi {nearest_taxi.taxi_id} allocated from {nearest_taxi.station} to {pickup_point}")
            return nearest_taxi
        print("All the taxis are occupied currently, please try again later!")
        return None
    
    # First 5kms cost rs.100 and remaining kms each cost rs.10.
    def calculate_travel_fare(self, pickup_point, drop_point, routes):
        station_travelled = abs(routes.index(pickup_point) - routes.index(drop_point))
        distance = station_travelled * 15

        if distance <= 15:
            return 100
        
        extra_distance = distance - 5
        extra_fare = extra_distance * 10
        total_fare = 100 + extra_fare
        return total_fare

    def confirm_booking(self, allocated_taxi, customer_name, pickup_point, drop_point, pickup_time, drop_time, routes):
        booking_id = generate_id('BTX')
        amount = self.calculate_travel_fare(pickup_point, drop_point, routes)
        new_booking = BookTaxi(booking_id, allocated_taxi.taxi_id, customer_name, pickup_point, drop_point, pickup_time, drop_time, amount)
        self.bookings[new_booking] = new_booking
        allocated_taxi.earnings+=amount
        print(f'Hey {customer_name}, your booking is confirmed and your booking id: {booking_id}')
        return True
    
    def book_taxi(self, routes, customer_name, pickup_point, drop_point, pickup_time, drop_time):
       allocated_taxi = self.taxi_allocate(pickup_point, routes)
       if allocated_taxi:
           confirm_booking = self.confirm_booking(allocated_taxi, customer_name, pickup_point, drop_point, pickup_time, drop_time, routes) 
           if confirm_booking:
               hops = abs(routes.index(pickup_point) - routes.index(drop_point))
            #  for simplicity of program, we have set travel time to be 30 seconds for each station taxi travel. 
               thread_sleep_time = hops * 30
               threading.Thread(target=self.free_taxi, args=(allocated_taxi, drop_point, thread_sleep_time), daemon=True).start()
               return  
       return
    
    def print_all_taxis(self):
        taxis = [taxi for taxi in self.taxis]
        if taxis:
            for taxi in taxis:
                print(f'Taxi id:{taxi.taxi_id}\tStation:{taxi.station}\tStatus:{taxi.status}\tEarnings:{taxi.earnings}')
        else:
            print('No taxis available!')
    
    def add_taxi(self):
        taxi_id = generate_id('TX')
        new_taxi = Taxi(taxi_id)
        self.taxis.append(new_taxi)
        print(f'New taxi added successfully!')
    
    def search_booking(self, taxi_id):
       taxi = [taxi for taxi in self.taxis if taxi.taxi_id == taxi_id]
       if not taxi:
          return print('There is no taxi with this id')
       
       print(f'TAX-ID: {taxi_id}\t TOTAL EARNINGS: {taxi[0].earnings}\n*****')
       found_booking = [booking for booking in self.bookings if booking.taxi_id == taxi_id]
       if not found_booking:
           return print('There is no booking yet for this taxi')
       for booking in found_booking:
           print(f'BOOKING-ID: {booking.booking_id}\t PICKUP POINT: {booking.pickup_point}\t DROP POINT: {booking.drop_point}\t PICKUP TIME: {booking.pickup_time}\t DROP TIME: {booking.drop_time}\t AMOUNT: {booking.amount}')

    # Using the concept of thread, 'occupied' taxis will be freed automatically.
    def free_taxi(self, taxi, drop_point, thread_sleep_time):
        time.sleep(thread_sleep_time)
        if self.lock:
            taxi.status = 'free'
            taxi.station = drop_point
            print(f'Taxi - {taxi.taxi_id} is free now and available at station: {drop_point}')

        


