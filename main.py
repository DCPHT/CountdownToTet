from distutils.log import debug
from flask import Flask, jsonify, request, render_template
from views import views

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

app.register_blueprint(views, url_prefix='/views')

@app.route('/security', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'date':'FEB 1, 2022 00:00:00'}
        return jsonify(message) 

app.run(host='0.0.0.0', debug=True)
