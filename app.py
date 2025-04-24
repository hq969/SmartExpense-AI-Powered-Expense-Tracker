from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("ai_model/model.pkl", "rb"))
vectorizer = pickle.load(open("ai_model/vectorizer.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_text = data['text']
    vect = vectorizer.transform([input_text])
    prediction = model.predict(vect)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
