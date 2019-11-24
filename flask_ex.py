from flask import Flask, render_template, request
from tonal_analizer import tonal_analize

app = Flask(__name__)

@app.route('/')
def hey():
	return 'Luck_pro team!'

@app.route('/map')
def digital_map():
	k = []

	for i in square_centers():
		k1 = 0
		for post in posts_get(i):
			k1 += tonal_analizer(post)
		k.append(k1)

	district = request.args.get('district', '')
	squares_id = []
	districts = []
	
	if district in districts:
		squares_id = districts_id[district]

	return render_template('rectangle.html', squares_id=str(squares_id), colors=k)

if __name__ == '__main__':
	app.run()