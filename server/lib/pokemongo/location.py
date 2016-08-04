from geopy.geocoders import GoogleV3
from s2sphere import CellId, LatLng
from custom_exceptions import GeneralPogoException
import gpxpy.geo


# Wrapper for location
class Location(object):
    def __init__(self, locationLookup, geo_key, noop=False):
        # Blank location
        if noop:
            self.noop = True
            self.geo_key = None
            self.locator = None
            self.latitude = None
            self.longitude = None
            self.altitude = None
            return

        self.noop = False
        self.geo_key = geo_key
        self.locator = GoogleV3()
        if geo_key:
            self.locator = GoogleV3(api_key=geo_key)

        self.latitude, self.longitude, self.altitude = self.setLocation(locationLookup)

    def __str__(self):
        s = 'Coordinates: {} {} {}'.format(
            self.latitude,
            self.longitude,
            self.altitude
        )
        return s

    @staticmethod
    def getLatLongIndex(latitude, longitude):
        return CellId.from_lat_lng(
            LatLng.from_degrees(
                latitude,
                longitude
            )
        ).id()

    @staticmethod
    def getDistance(*coords):
        return gpxpy.geo.haversine_distance(*coords)

    @staticmethod
    def Noop():
        return Location(None, None, noop=True)

    def setLocation(self, search):
        try:
            geo = self.locator.geocode(search)
        except Exception as e:
            raise GeneralPogoException('Error in Geo Request, with exception: {0}'.format(e))
        else:
            return geo.latitude, geo.longitude, geo.altitude

    def setCoordinates(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def getCoordinates(self):
        return self.latitude, self.longitude, self.altitude

    def getCells(self, radius=10, bothDirections=True):
        origin = CellId.from_lat_lng(
            LatLng.from_degrees(
                self.latitude,
                self.longitude
            )
        ).parent(15)

        # Create walk around area
        walk = [origin.id()]
        right = origin.next()
        left = origin.prev()

        # Double the radius if we're only walking one way
        if not bothDirections:
            radius *= 2

        # Search around provided radius
        for _ in range(radius):
            walk.append(right.id())
            right = right.next()
            if bothDirections:
                walk.append(left.id())
                left = left.prev()

        # Return everything
        return sorted(walk)