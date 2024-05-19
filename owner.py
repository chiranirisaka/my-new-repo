from bus import Bus
from route import Route

class Owner:
    def __init__(self):
        self.buses = []
        self.routes = []

    def add_bus(self, bus_id, seats):
        bus = Bus(bus_id, seats)
        self.buses.append(bus)
        print(f"Bus {bus_id} with {seats} seats added.")

    def view_buses(self):
        for bus in self.buses:
            print(bus)

    def add_route(self, route_id, origin, destination):
        route = Route(route_id, origin, destination)
        self.routes.append(route)
        print(f"Route {route_id} from {origin} to {destination} added.")

    def view_routes(self):
        for route in self.routes:
            print(route)
