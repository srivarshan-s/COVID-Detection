from geopy import Nominatim
import haversine as hs


def getCoords(place):
    g = Nominatim(user_agent='myGeocoder', timeout=100)
    location = g.geocode(place)
    return (location.latitude, location.longitude)


def getDistance(place1, place2):
    place1Coords = getCoords(place1)
    place2Coords = getCoords(place2)
    return hs.haversine(place1Coords, place2Coords)
