from geopy import Nominatim
import haversine as hs


def getCoords(place):
    g = Nominatim(user_agent="myGeocoder", timeout=100)
    location = g.geocode(place)
    return (location.latitude, location.longitude)


def getXCoords(place):
    g = Nominatim(user_agent="myGeocoder", timeout=100)
    location = g.geocode(place)
    return location.latitude


def getYCoords(place):
    g = Nominatim(user_agent="myGeocoder", timeout=100)
    location = g.geocode(place)
    return location.longitude


def getDistance(place1, place2):
    place1Coords = (place1['xcoord'], place1['ycoord'])
    place2Coords = (place2['xcoord'], place2['ycoord'])
    return hs.haversine(place1Coords, place2Coords)
