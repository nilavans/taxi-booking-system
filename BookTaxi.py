class BookTaxi:
    def __init__(self, booking_id, taxi_id, name, pickup_point, drop_point, pickup_time, drop_time, amount):
        self.booking_id = booking_id
        self.taxi_id = taxi_id
        self.customer_name = name
        self.pickup_point = pickup_point
        self.drop_point = drop_point
        self.pickup_time = pickup_time
        self.drop_time = drop_time
        self.amount = amount