class Customer:
    def __init__(self, name):
        self.name = name

    def book_ticket(self, bus):
        if bus.book_ticket(1):  # Assuming booking one seat at a time
            print(f"{self.name} successfully booked a ticket on Bus {bus.bus_id}")
        else:
            print(f"Sorry, {self.name}. No available seats on Bus {bus.bus_id}.")

    def __str__(self):
        return f"Customer Name: {self.name}"
