# main.py

from customer import Customer
from owner import Owner
from bus import Bus

def main():
    # Create owner
    owner = Owner(owner_id=1, name="John Doe")
    
    # Create buses
    bus1 = Bus(bus_id=101, seats=40)
    bus2 = Bus(bus_id=102, seats=30)
    
    # Owner adds buses
    owner.add_bus(bus1)
    owner.add_bus(bus2)
    
    # View all buses
    print("\nBuses managed by owner:")
    owner.view_buses()
    
    # Create customers
    customer1 = Customer(customer_id=1, name="Alice")
    customer2 = Customer(customer_id=2, name="Bob")
    
    # Customers book tickets
    print("\nBooking tickets:")
    customer1.book_tickets(bus1, 5)  # Successful booking
    customer2.book_tickets(bus1, 37) # Unsuccessful booking due to insufficient seats

    # View available seats after booking
    print("\nAvailable seats after booking:")
    owner.view_buses()

if __name__ == "__main__":
    main()
 
