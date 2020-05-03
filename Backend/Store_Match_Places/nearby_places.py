import googlemaps
import pprint
import time
import html2text
# from GoogleMapsAPIKey import get_my_key

lat_lon = '-33.8670522,151.1957362'

#define API
API_KEY = 'AIzaSyA950W2SYIsCt6uvuFNItJmRGetaxY4W30'

gmaps = googlemaps.Client(key = API_KEY)


def get_nearby_places(placeId, serviceType, radius=24000 ):
    center = gmaps.place(place_id=placeId)
    places_result = gmaps.places_nearby(location=center['result']['geometry']['location'], radius=radius, type=serviceType)
    stored_results = []
    while len(places_result['results']) >= 20 and len(stored_results) <= 50:
        for place in places_result['results']:
            # define the place id, needed to get place details. Formatted as a string.
            my_place_id = place['place_id']
            # define the fields you would liked return. Formatted as a list.
            my_fields = ['name', 'formatted_phone_number', 'formatted_address', 'website', 'place_id']
            # make a request for the details.
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            stored_results.append(places_details['result'])
        time.sleep(1)
        if len(stored_results) < 40:
            places_result  = gmaps.places_nearby(page_token = places_result['next_page_token'])
        
    # stored_results return as list of dictionaries each with 
    # name, phone number, address, website, and place_id
    return stored_results
#test
#result = get_nearby_places(placeId='ChIJ80C0mkCa44kR4pqBL_NclhA', serviceType='restaurant' )
#print(result)
    

