# neo_restaurant.py

import ast, collections

class Restaurant:
	def __init__(self, name, email, address, food_and_amt_to_give):
		self.name = name
		self.email = email
		self.address = address
		self.food_and_amt_to_give = food_and_amt_to_give

def get_restaurants():
	restaurant_dicts = []
	with open("restaurant_data.txt", "r") as res_data:
		for line in res_data.readlines():
			dict_line = ast.literal_eval(line)
			restaurant_dicts.append(dict_line)
	return restaurant_dicts

def add_restaurant(restaurant):
	restaurant = restaurant.__dict__
	restaurants = get_restaurants()
	restaurants.append(restaurant)
	restaurants = [x for n, x in enumerate(restaurants) if x not in restaurants[:n]]
	with open("restaurant_data.txt", "w") as res_file:
		for rest in restaurants:
			res_file.write(f"{rest}\n")

if __name__ == "__main__":
	foods = {
		"Pizza Rolls": 24,
		"Pepperoni Slices": 89,
		"Salad": 15
	}

	bertuccis = Restaurant("Berticci's", "bertuccis@gmail.com", "Our Address", foods)
	add_restaurant(bertuccis)
	b = get_restaurants()

	for thing in b:
		print(thing)