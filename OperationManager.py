from datetime import datetime, timedelta
from TaxiManager import *
from Utils import validate_input, get_input

class OperationManager:
    def __init__(self):
        # Initialise with default routes.
        self.routes = ['A', 'B', 'C', 'D']
        self.TaxiManager = TaxiManager()

    def print_options(self):
        print('Available Options: ')
        options = [
            '1. Add taxi',
            '2. Book a taxi',
            '3. Print taxi details',
            '4. Add new route',
            '5. Print booking history of a taxi',
            '6. End the program'
            ]
        print('\n'.join(options))
        return self.get_choice(len(options))
        
    def get_choice(self, total_options):
        message = f"Enter your choice from 1 to {total_options} \n"
        return validate_input(message, 1, total_options)
    
    def calculate_drop_time(self, pickup_point, drop_point, pickup_time_str):
        if pickup_point not in self.routes or drop_point not in self.routes:
            return print(f"Invalid pickup or drop point!")
        
        hops = abs(self.routes.index(pickup_point) - self.routes.index(drop_point))
        travel_time = hops * 60
        pickup_time = datetime.strptime(pickup_time_str, '%H:%M')
        drop_time = pickup_time + timedelta(minutes=travel_time)

        return datetime.strftime(drop_time, '%H:%M')

    def add_taxi(self):
        self.TaxiManager.add_taxi()
    
    def book_taxi(self):
        customer_name = get_input('Enter customer name: ')
        pickup_point = get_input("Enter pickup point (e.g., 'A', 'B') : ")
        drop_point = get_input("Enter drop point (e.g., 'A', 'B') : ")
        pickup_time = get_input('Enter pickup time (HH:MM): ')
        drop_time = self.calculate_drop_time(pickup_point, drop_point, pickup_time)
        self.TaxiManager.book_taxi(self.routes, customer_name, pickup_point, drop_point, pickup_time, drop_time)
    
    def print_all_taxis(self):
        return self.TaxiManager.print_all_taxis()
    
    def add_route(self):
        new_route = get_input("Enter the name of new station (e.g., 'A'): ")
        for route in self.routes:
            if  route.name == new_route:
                return print(f"The {new_route} already exists!")
        self.routes.append(new_route)
        print('Route is added successfully')

    def search_booking(self):
        taxi_id = get_input('Enter a taxi id you wish to view (i.e., booking history): ')
        self.TaxiManager.search_booking(taxi_id)

    def run(self):
        while True:
            choice = self.print_options()
            match choice:
                case 1:
                    self.add_taxi()
                case 2:
                    self.book_taxi()
                case 3:
                    self.print_all_taxis()
                case 4:
                    self.add_route()
                case 5:
                    self.search_booking()
                case 6:
                    print('Thanks for using. Ending the program!')
                    break
            print('************************************************************')