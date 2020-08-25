import flask
import pickle
import pandas as pd

'''
bath_entry = 4
bed_entry = 4
square_feet_entry = 2580
lot_size_entry = 2613
year_built_entry = 1920
latitude_entry = 45.499533
longitude_entry = -122.675113
'''
with open(f'model/finalized_model.sav', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        baths = flask.request.form['baths']
        beds = flask.request.form['beds']
        square_feet = flask.request.form['square_feet']
        latitude = flask.request.form['latitude']
        longitude = flask.request.form['longitude']
        input_variables = pd.DataFrame([[baths, beds, square_feet, latitude, longitude]],
                                       columns=['BATHS', 'BEDS', 'SQUARE FEET', 'LATITUDE', 'LONGITUDE'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('main.html',
                                     original_input={'Baths':baths,
                                                     'Beds':beds,
                                                     'Square Feet':square_feet,
                                                     'Latitude':latitude,
                                                     'Longitude':longitude},
                                     result=prediction,
                                     )
if __name__ == '__main__':
    app.run()