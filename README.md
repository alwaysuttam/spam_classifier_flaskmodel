House Price Prediction Web Application
This web application estimates the price of a house based on various parameters such as location, square footage (sqft), number of bedrooms (BHK), and number of bathrooms (bath). The model is pre-trained and the application serves predictions using this model.

Project Structure
app.py: The main Flask application script.
templates/: Directory containing HTML template(s) for the web pages.
index.html: The main page where users input the data and view predictions.
data/: Directory containing necessary data files.
columns.json: JSON file containing the data columns used by the model.
bhpp.pickle: Pickle file containing the trained model.
Setup Instructions
Prerequisites
Python 3.x
Flask
Numpy
Scikit-learn (for loading the pickle model)
Installation
Clone the repository or download the project files.

Ensure you have Python installed on your machine.

Install the necessary Python packages using pip:

bash
Copy code
pip install flask numpy scikit-learn
Running the Application
Navigate to the project directory.

Run the Flask application:

bash
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:5000/.

Application Details
Routes
/: The main page where users can input data and view the predicted house price.
/predict: Endpoint to handle form submission and return the estimated price.
Data Files
columns.json: This file contains the list of all columns used in the model. It helps in mapping the input features to the model's expected format.

Example structure:

json
Copy code
{
  "data_columns": ["sqft", "bath", "bhk", "location1", "location2", ...]
}
bhpp.pickle: This is a serialized (pickled) file containing the pre-trained house price prediction model.

Index Page (index.html)
The index page contains a form for users to input the required parameters:

Location (dropdown)
Square Footage (input box)
Number of BHK (input box)
Number of Bathrooms (input box)
Upon form submission, the data is sent to the /predict endpoint for processing, and the predicted price is rendered on the same page.

Prediction Logic
The input data from the form is parsed and validated.
The location is checked against the list of known locations.
An input feature vector is constructed based on the input parameters.
The model predicts the price based on the input features.
The predicted price is displayed on the index page.
Error Handling
If an invalid location is entered, an error message is returned.
Example Usage
Start the Flask server by running python app.py.
Navigate to http://127.0.0.1:5000/.
Fill out the form with the house details and submit.
View the estimated price on the same page.
