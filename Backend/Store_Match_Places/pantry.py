# pantry.py

import ast, collections

class Pantry:
	def __init__(self, name, email, address, food_and_amt_needed):
		self.name = name
		self.email = email
		self.address = address
		self.food_and_amt_needed = food_and_amt_needed

def get_pantries():
	restaurant_dicts = []
	with open("pantry_data.txt", "r") as res_data:
		for line in res_data.readlines():
			dict_line = ast.literal_eval(line)
			restaurant_dicts.append(dict_line)
	return restaurant_dicts

def add_pantry(pantry):
	pantry = pantry.__dict__
	pantries = get_pantries()
	pantries.append(pantry)
	pantries = [x for n, x in enumerate(pantries) if x not in pantries[:n]]
	with open("pantry_data.txt", "w") as pan_file:
		for pan in pantries:
			pan_file.write(f"{pan}\n")

if __name__ == "__main__":
	foods_needed = {
		"Beans": 24,  # ounces
		"Pepperoni Slices": 89,  # grams
		"Salad": 15  # pounds or kilos
	}

	helping_place = Pantry("Helper", "good_pantry@gmail.com", "Our Address", foods_needed)
	add_pantry(helping_place)
	b = get_pantries()

	for thing in b:
		print(thing)