from flask import Flask, render_template, request
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)

# Load pre-trained model and vectorizer
tfidf = pickle.load(open('data/vectorizer.pkl', 'rb')) ## data\model.pkl
model = pickle.load(open('data/model.pkl', 'rb'))

# Initialize NLTK components
nltk.download('punkt')
nltk.download('stopwords')
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))


def transform_text(text):
    text = text.lower()  # Convert to lowercase
    text = nltk.word_tokenize(text)  # Tokenization

    # Remove special characters and filter out stopwords
    words = [ps.stem(word) for word in text if word.isalnum() and word not in stop_words]

    return " ".join(words)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    input_sms = request.form['message']
    transform_sms = transform_text(input_sms)

    sms_vector = tfidf.transform([transform_sms])
    result = model.predict(sms_vector)[0]

    if result == 1:
        prediction = 'Spam'
    else:
        prediction = 'Not Spam'

    return render_template('predict.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
