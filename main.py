from flask import Flask, jsonify, request, render_template
from views import views
from calc_tet import calc_tet, get_data
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
        tet_each_year = calc_tet()
        message = {'date': tet_each_year}
        return jsonify(message)


@app.route('/calcCalender', methods=['GET', 'POST'])
def convert_date_time():
    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        data = get_data()
        message = {'date': data}
        return jsonify(message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
