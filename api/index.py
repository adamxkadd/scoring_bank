from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

# @app.route('/test', methods =['GET', 'POST'] )
@app.route('/test')
def test():
	# my_data = {'text' : 'texte', 'int' : 123, 'timestamp' : time.time()}
	# my_data_json = json.dumps(my_data)
	# my_data = 1234
	# return str(my_data)	


	my_data = {'text' : 'texte', 'int' : 123, 'message' : 'Hello, Flask!'}
	# Utilisez jsonify pour convertir le dictionnaire en JSON et renvoyez-le avec un code de statut 200 (OK)
	return jsonify(my_data)
