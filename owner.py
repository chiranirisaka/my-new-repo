# owner.py

from bus import Bus

class Owner:
    def __init__(self, owner_id, name):
        self.owner_id = owner_id
        self.name = name
        self.buses = []

    def add_bus(self, bus):
        self.buses.append(bus)
        print(f"Bus {bus.bus_id} added by {self.name}")

    def view_buses(self):
        for bus in self.buses:
            print(bus)

    def __str__(self):
        return f"Owner ID: {self.owner_id}, Name: {self.name}"
 
