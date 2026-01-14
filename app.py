from flask import Flask, request, jsonify
import sys
sys.path.append('server')  # Import server/util
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    util.load_saved_artifacts()
    return jsonify({'locations': util.get_location_names()})

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    return jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
