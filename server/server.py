from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get-location')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict-price', methods=["POST"])
def predict_price():
    location = request.form['location']
    area = float(request.form['area'])
    bhk = int(request.form['bhk'])
    gym = int(request.form['gym'])
    lift = int(request.form['lift'])
    car_parking = int(request.form['car_parking'])
    security = int(request.form['security'])
    playground = int(request.form['playground'])
    swimming_pool = int(request.form['swimming_pool'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, area, bhk, gym, lift, car_parking, security, playground,
                                                    swimming_pool)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Flask Server for Home Price Prediction")
    util.load_saved_artifacts()
    app.run()
