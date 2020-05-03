HOW TO USE THIS CODE:

Dependencies:
"pip3 install geopy"
In order to make geopy work, you must run the "Install Certificates" script included with your Python installation. You can probably find it by searching for it in Finder.

By importing the pantry class, you can make a pantry object representing a store.
The same applies for the restaurant class.

To add a pantry or a restaurant to the store database, call the "add_pantry" or "add_restaurant" function from its respective module.
To get a list of all pantries or restaurants, call the get_pantries or get_restaurants functions.

If you wish to find the nearest food pantry for a given restaurant, call the "main" function in module "find_nearest.py", while supplying an address of the origin location, and the type of location being searched for (with this being "pantry") here, and vice versa for a restaurant.
