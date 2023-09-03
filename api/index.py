from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/about')
def test():
    return 'TEST'
  
@app.route('/', methods =['GET', 'POST'] )
def home():
	my_data = {'text' : 'texto', 'int' : 55555, 'message' : 'Helloxxx, Flask!'}
	return jsonify(my_data)
