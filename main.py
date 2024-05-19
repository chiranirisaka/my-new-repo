# main.py

from owner import Owner
from customer import Customer

def main():
    owner = Owner()
    owner.add_bus("Bus1", 50)
    owner.add_bus("Bus2", 30)
    owner.add_route("Route1", "CityA", "CityB")
    owner.add_route("Route2", "CityC", "CityD")

    print("\nViewing all buses:")
    owner.view_buses()
    print("\nViewing all routes:")
    owner.view_routes()


    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    print("\nBooking tickets:")
    customer1.book_ticket(owner.buses[0])
    customer2.book_ticket(owner.buses[1])
    customer2.book_ticket(owner.buses[1])

    print("\nViewing all buses after bookings:")
    owner.view_buses()

if __name__ == "__main__":
    main()


