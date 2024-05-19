# customer.py

from bus import Bus

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def book_tickets(self, bus, num_seats):
        if bus.book_ticket(num_seats):
            print(f"{self.name} successfully booked {num_seats} seat(s) on Bus {bus.bus_id}")
        else:
            print(f"Sorry, {self.name}. Not enough seats available on Bus {bus.bus_id}.")

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}"

