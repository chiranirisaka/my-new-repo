class Bus:
    def __init__(self, bus_id, seats):
        self.bus_id = bus_id
        self.seats = seats
        self.available_seats = seats

    def book_ticket(self, num_seats):
        if num_seats <= self.available_seats:
            self.available_seats -= num_seats
            return True
        return False

    def get_available_seats(self):
        return self.available_seats

    def __str__(self):
        return f"Bus ID: {self.bus_id}, Seats: {self.seats}, Available Seats: {self.available_seats}"

