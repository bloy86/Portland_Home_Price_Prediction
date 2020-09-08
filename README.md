# Portland Home Price Prediction

#### -- Project Status: Completed

## Objective
The purpose of this project was to predict selling prices of homes in the city of Portland, Oregon.  Although there are other algorithms to predict home prices (e.g., Zillow, Redfin), these predict value and not necessarily selling price.  An additional objective was to understand what parameters influence selling price, as the other algorithms are proprietary and the inputs are not known. 

### Methods Used
* Machine Learning
* Data Visualization
* Predictive Modeling

### Technologies
* Python
* Pandas, jupyter, scikit-learn 
* HTML
* CSS
* Javascript
* Heroku


## Project Description
I pulled data from Redfin of single-family homes that sold in the last 6 months within Portland, Oregon.  The pull was completed on August 20, 2020 so we had homes that sold February 24-August 20, 2020.  Redfin limits data pulls to 250 homes, so I needed to complete a pull for each Portland zip code to get a full dataset of Portland.  After dropping outliers and homes missing descriptive variables, we had a dataset of 2,294 homes and 12 possible predictor variables, plus the selling price. 

Our initial model included the following variables:
* Number of bedrooms
* Number of bathrooms
* Square feet of home
* Square feet of the lot
* Year the home was built

Our initial model scores were low.  I parsed the existing address variable to create several new variables, which improved the model score. These variables were:
* Westside/Eastside location Ð Homes on the west side of the Willamette river tend to have better views of the Cascade mountain range, but also have higher property taxes, both of which may impact selling price.
* Numbered/Alphabetical street Ð In Portland, numbered streets (e.g., NE 22nd) run North-South and tend to be quieter, whereas alphabetical streets (e.g, NE Halsey) run East-West and are often busier, multi-lane travel corridors. The busyness or quietness of a street could impact home value.

The final model had a score of 0.68.  Although this is not as high as our team wanted, We are happy that we could improve the score from an initial 0.60 by creating new variables from the existing data.  

## Deliverables
* [Application](https://homeprice-prediction-pdx.herokuapp.com/application)
* To run, visit the application site linked above and test using input values of homes located in the city of Portland, Oregon. 

![](machine%20learning%20code/Home%20Price%20App.png)

## Team Members

|Name     |  GibHub Handle   | 
|---------|-----------------|
|Blaine Gobler | goblebla   |
|Bryan Loy | bloy86   |
|Peter Nguyen | nguyenpe17  |
|Walter Stern | wstern1   |

## Contact
* Bryan Loy, linkedin.com/in/bryanloy

