from flask import Flask, render_template, request
from tonal_analizer import tonal_analize

app = Flask(__name__)

@app.route('/')
def hey():
	return 'Luck_pro team!'

@app.route('/map')
def digital_map():
	district = request.args.get('district', '')
	squares_id = []
	districts = []
	
	if district in districts:
		squares_id = districts_id[district]

	return render_template('rectangle.html', squares_id=str(squares_id))

if __name__ == '__main__':
	app.run()