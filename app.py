import numpy as np
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/application')
def application():    
    return render_template('main.html')

@app.route('/predict',methods=['POST', 'GET'])
def predict():

    bath_entry = float(request.form.get('baths'))
    bed_entry = float(request.form.get('beds'))
    square_feet_entry = float(request.form.get('square_feet'))
    lot_size_entry = float(request.form.get('lot_size'))
    year_built_entry = float(request.form.get('year_built'))
    westside_1_west_0_east = float(request.form.get('w_or_e'))
    street_1_num_0_alpha = float(request.form.get('number_or_alphabetical'))

    home_value = 1812.95 + (bath_entry *(70945.12)) + (bed_entry *(-21601.08)) + (square_feet_entry *(179.82)) + (lot_size_entry *(4.17)) + (year_built_entry * (39.08)) + (street_1_num_0_alpha *(22541.99)) + (westside_1_west_0_east *(27364.42))
    print (home_value)
    output = round(home_value, 2)

    return render_template('main.html', prediction_text='Bleep bloop... home price predicted to be ${}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)