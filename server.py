from flask import Flask, render_template, request
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)


try:
    tfidf = pickle.load(open('data/vectorizer.pkl', 'rb'))
    model = pickle.load(open('data/model.pkl', 'rb'))
except FileNotFoundError:
    print("Model files not found. Make sure 'data/vectorizer.pkl' and 'data/model.pkl' exist.")


nltk.download('punkt')
nltk.download('stopwords')
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))


def transform_text(text):
    text = text.lower()  
    text = nltk.word_tokenize(text)  

    
    words = [ps.stem(word) for word in text if word.isalnum() and word not in stop_words]

    return " ".join(words)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_sms = request.form['message']
        transform_sms = transform_text(input_sms)

        sms_vector = tfidf.transform([transform_sms])
        result = model.predict(sms_vector)[0]

        if result == 1:
            prediction = 'Spam'
        else:
            prediction = 'Not Spam'

        return render_template('index.html', prediction=prediction, message=input_sms)
    except:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
