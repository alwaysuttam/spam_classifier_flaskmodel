# SMS Spam Detection Web Application

This is a Flask web application that classifies SMS messages as "Spam" or "Not Spam" using a pre-trained machine learning model. The application processes the input text using Natural Language Processing (NLP) techniques and predicts the message category.

## Project Structure

app.py: The main Flask application script.

templates/: Directory containing HTML templates for the web pages.
index.html: The main page where users can input the SMS message and view the prediction.
error.html: The error page shown if any issues occur during processing.

data/: Directory containing the necessary model files.

vectorizer.pkl: Pickle file containing the pre-trained TF-IDF vectorizer.

model.pkl: Pickle file containing the pre-trained classification model.

## Setup Instructions

**Prerequisites**

Python 
Flask
NLTK
Scikit-learn
Pickle

**Installation**

Clone the repository:

git clone https://github.com/uttam-bn/spam_classifier_flaskmodel.git
cd sms-spam-detection
code . # to open in Visual studio 

Ensure you have Python installed on your machine.

Install the necessary Python packages using pip:

pip install flask nltk scikit-learn

Download the NLTK data required for the application:

python
Copy code
import nltk
nltk.download('punkt')
nltk.download('stopwords')
Running the Application
Navigate to the project directory.

**Run the Flask application:**

python app.py
Open your web browser and go to http://127.0.0.1:5000/.

**screenshots of the project**
![alt text](<Screenshot (54).png>)