import googlemaps
import pprint
import time
import html2text
# from GoogleMapsAPIKey import get_my_key

lat_lon = '-33.8670522,151.1957362'

#define API
API_KEY = 'AIzaSyA950W2SYIsCt6uvuFNItJmRGetaxY4W30'

gmaps = googlemaps.Client(key = API_KEY)

places_result = gmaps.places_nearby(location=lat_lon, radius=40000, type='restaurant')

time.sleep(3)

place_result  = gmaps.places_nearby(page_token = places_result['next_page_token'])

stored_results = []

# loop through each of the places in the results, and get the place details.      
for place in places_result['results']:

    # define the place id, needed to get place details. Formatted as a string.
    my_place_id = place['place_id']

    # define the fields you would liked return. Formatted as a list.
    my_fields = ['name','formatted_phone_number','website', 'adr_address']

    # make a request for the details.
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)

    # print the results of the details, returned as a dictionary.
    pprint.pprint(places_details['result'])
    html_address = html2text.HTML2Text()
    readable_address = html_address.handle(places_details['result'].get("adr_address"))
    print(readable_address)

    # store the results in a list object.
    stored_results.append(places_details['result'])
    stored_results.append(readable_address)
