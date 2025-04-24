from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open('ai_model/model.pkl', 'rb'))
vectorizer = pickle.load(open('ai_model/vectorizer.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        expense_text = request.form['expense']
        vect_text = vectorizer.transform([expense_text])
        prediction = model.predict(vect_text)
        return render_template('index.html', prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
