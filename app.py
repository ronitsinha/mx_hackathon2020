import flask as fl
import json

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

@app.route('/handle_name/<user_type>', methods=['POST'])
def handle_name (user_type=None):

	if not fl.request.form['name'] == '':
		return fl.redirect( fl.url_for(user_type, name=fl.request.form['name']) )

	return fl.redirect( fl.url_for(user_type) )

@app.route('/handle_foodbank_request', methods=['POST'])
def handle_foodbank_request ():
	data = json.loads(fl.request.form['js_data'])

	app.logger.debug(data)

	return None