from bus import Bus


class Owner:
    def __init__(self):
        self.buses = []


    def add_bus(self, bus_id, seats):
        bus = Bus(bus_id, seats)
        self.buses.append(bus)
        print(f"Bus {bus_id} with {seats} seats added.")

    def view_buses(self):
        for bus in self.buses:
            print(bus)
