import flask as fl
import json
import googlemaps
import pprint
import time
import html2text
# from GoogleMapsAPIKey import get_my_key

# lat_lon = '-33.8670522,151.1957362'

#define API
API_KEY = 'AIzaSyA950W2SYIsCt6uvuFNItJmRGetaxY4W30'

gmaps = googlemaps.Client(key = API_KEY)


def get_nearby_places(placeId, serviceType, radius=24000 ):
    center = gmaps.place(place_id=placeId)
    places_result = gmaps.places_nearby(location=center['result']['geometry']['location'], radius=radius, type=serviceType)
    stored_results = []
    while len(places_result['results']) >= 20 and len(stored_results) <= 10:
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
    

app = fl.Flask(__name__, static_folder='static')

@app.route('/')
def index ():
	return fl.render_template('index.html')

@app.route('/restaurant')
@app.route('/restaurant/<name>/')
def restaurant (name=None):
	return fl.render_template('restaurant.html', name=name)

@app.route('/foodbank')
@app.route('/foodbank/<name>')
def foodbank (name=None):
	return fl.render_template('foodbank.html', name=name)

@app.route('/handle_foodbank_request', methods=['POST'])
def handle_foodbank_request ():
	data = json.loads(fl.request.form['js_data'])

	app.logger.debug(data)

	return ''

@app.route('/handle_location/<user_type>', methods=['POST'])
def handle_location (user_type=None):
	location = fl.request.form['location'] 

	name = gmaps.place(place_id=location, fields=['name'])

	service_type = 'restaurant' if user_type=='foodbank' else 'foodbank'

	nearby = get_nearby_places(location, 'restaurant')

	app.logger.debug(nearby)

	with open('static/data.js', 'w') as json_file:
  		json_file.write( 'data=JSON.parse(String(%s))' % json.dumps(nearby) )

	return fl.redirect(fl.url_for(user_type, name=name['result']['name']))
