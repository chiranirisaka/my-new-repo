class Route:
    def _init_(self, route_id, origin, destination):
        self.route_id = route_id
        self.origin = origin
        self.destination = destination

    def _str_(self):
        return f"Route ID: {self.route_id}, Origin: {self.origin}, Destination: {self.destination}"
