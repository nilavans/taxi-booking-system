class Taxi:
    def __init__(self, id, station = 'A', status= 'free', earnings = 0):
        self.taxi_id  = id
        self.station = station
        self.status = status
        self.earnings = earnings