import flask as fl
import json
import googlemaps

app = fl.Flask(__name__, static_folder='static')

@app.route('/')
def index ():
	return fl.render_template('index.html')

@app.route('/restaurant')
@app.route('/restaurant/<name>')
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

	return None

@app.route('/handle_location/<user_type>', methods=['POST'])
def handle_location (user_type=None):
	location = fl.request.form['location'] 	

	app.logger.debug(location)

	return ''