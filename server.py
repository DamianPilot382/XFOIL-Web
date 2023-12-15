from flask import Flask, request, jsonify
from flask_cors import CORS
from Airfoil import compute
import numpy as np


####
# pip install Flask flask_cors
####

# creates a flask server for post requests
app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})

@app.route('/compute', methods=['POST'])
def compute_airfoil():
    data = request.get_json()
    vinf = float(data['v_inf'])
    aoa = float(data['aoa'])
    databuffer = np.array(data['data'])

    text, panel_geometry, geom_pts, control_pts, pressure = compute(vinf, aoa, databuffer)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True, port=5000)