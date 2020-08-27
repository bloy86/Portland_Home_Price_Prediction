import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

'''
bath_entry = 4
bed_entry = 4
square_feet_entry = 2580
lot_size_entry = 2613
year_built_entry = 1920
latitude_entry = 45.499533
longitude_entry = -122.675113
'''
app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction.round(decimals=2)

    return render_template('main.html', prediction_text='Price should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)