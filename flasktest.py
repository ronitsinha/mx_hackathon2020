from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_folder='static')

@app.route('/')
def index ():
	return render_template('index.html')

@app.route('/restaurant')
@app.route('/restaurant/<name>')
def restaurant (name=None):
	return render_template('restaurant.html', name=name)

@app.route('/foodbank')
def food_bank ():
	return 'Food Bank'

@app.route('/handle_data', methods=['POST'])
def handle_data ():
	return redirect('/restaurant/' + request.form['name'])