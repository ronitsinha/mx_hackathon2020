# calculate_distance.py

# must install certificates for this script to work

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import os

def cal_dist(addr_1, addr_2):
	geolocator = Nominatim()
	loc_1 = geolocator.geocode(addr_1)
	loc_2 = geolocator.geocode(addr_2)

	coord_1 = loc_1.latitude, loc_1.longitude
	coord_2 = loc_2.latitude, loc_2.longitude

	distance_btwn = geodesic(coord_1, coord_2).miles

	return distance_btwn

if __name__ == "__main__":
	loc_1 = "175 5th Avenue NYC"
	loc_2 = "23 Columbia Street, Watertown MA 02472"
	distance_apart = cal_dist(loc_1, loc_2)
	print(distance_apart)