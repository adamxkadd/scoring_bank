from flask import Flask

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
	my_data = 1234
	return str(my_data)	
