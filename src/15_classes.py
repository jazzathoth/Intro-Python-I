# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return 'Name: {self.name} \n' \
               'Lat: {self.lat} \n' \
               'Lon: {self.lon}'.format(self=self)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, lat, lon, size, name, difficulty):
        super().__init__(lat, lon, name)
        self.size = size
        self.difficulty = difficulty

    def __str__(self):
        return 'Name: {self.name} \n' \
               'Lat: {self.lat}\n' \
               'Lon: {self.lon}\n' \
               'Size: {self.size}\n' \
               'Difficulty: {self.difficulty}'.format(self=self)


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = Waypoint(lat=41.70505, lon=-121.51521, name='Catacombs')
print(waypoint.name, waypoint.lat, waypoint.lon)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(lat=44.052137, lon=-121.41556, size=2, name="Newberry Views", difficulty=1.5)

# Print it--also make this print more nicely
print(geocache)
