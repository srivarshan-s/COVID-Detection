from geopy import Nominatim
import haversine as hs


def getLatitude(place):
    g = Nominatim(user_agent='myGeocoder', timeout=100)
    location = g.geocode(place)
    return location.latitude


def getLongitude(place):
    g = Nominatim(user_agent='myGeocoder', timeout=100)
    location = g.geocode(place)
    return location.longitude


def getDistance(place1, place2):
    place1Coords = (getLatitude(place1), getLongitude(place1))
    place2Coords = (getLatitude(place2), getLongitude(place2))
    return hs.haversine(place1Coords, place2Coords)
