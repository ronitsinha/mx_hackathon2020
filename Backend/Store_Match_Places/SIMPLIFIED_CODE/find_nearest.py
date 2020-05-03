from restaurant import *
from pantry import *
from calculate_distance import cal_dist

# STORE TYPE: string - pantry or restaurant
# STORE NAME: string - examples include bertucci's pantry #1, etc
# EMAIL: string - examples include bertuccis@gmail.com, pantry@gmail.com, etc
# ADDRESS: string - must be put in the format of "building_number, street name, town name, shortened state name, zip code"
# FOOD AND AMT: dictionary - format of {food name: food amt, food name: food amt, etc}
def gather_info(store_type, store_name, email, address, food_and_amt):
	if store_type == "pantry":
		info_obj = Pantry(store_name, email, address, food_and_amt)
	elif store_type == "restaurant":
		info_obj = Pantry(store_name, email, address, food_and_amt)
	return info_obj


# search for parameters: pantry, or restaurant
def find_nearby_place(origin_address, search_for):
	
	distances = {}

	if search_for == "pantry":
		pantries = get_pantries()
		for pantry in pantries:
			dist_btwn = cal_dist(pantry["address"], origin_address)
			distances[pantry["email"]] = dist_btwn
		try:
			shortest_distance = min(distances.values())
		except TypeError:
			return None
		for email, distance in distances.items():
			if distance == shortest_distance:
				return email, distance

	elif search_for == "restaurant":
		restaurants = get_restaurants()
		for restaurant in restaurants:
			dist_btwn = cal_dist(restaurant["address"], origin_address)
			distances[restaurant["email"]] = dist_btwn

		print(f"Distances: {distances}")

		try:
			shortest_distance = min(distances.values())
		except TypeError:
			return None
		for email, distance in distances.items():
			if distance == shortest_distance:
				return email, distance

def make_email(type_place, email, distance):
	msg = f"""
	You have matched with a local {type_place}!
	Their email is {email}. They're around
	{int(distance)} miles away, and they need food.
	Good luck with getting in contact with them!
	"""
	return msg

def main(address, search_for):
	nearby_place = find_nearby_place(address, search_for)

	if nearby_place is None:
		print("We're sorry, but our services are not available in your location.")
	else:
		for_email = ["restaurant", nearby_place[0], nearby_place[1]]
		email = make_email(*for_email)
		print(email)

if __name__ == "__main__":
	main("25 Chestnut St, Watertown, MA, 02472", search_for = "pantry")
