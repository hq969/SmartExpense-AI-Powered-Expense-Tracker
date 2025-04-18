from flask import Flask, request, jsonify
import sqlite3
import pickle
from datetime import datetime

app = Flask(__name__)

# Load AI model
with open('ai_model/model.pkl', 'rb') as m:
    model = pickle.load(m)

with open('ai_model/vectorizer.pkl', 'rb') as v:
    vectorizer = pickle.load(v)

# Initialize SQLite DB
def init_db():
    with sqlite3.connect("expenses.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            amount REAL,
            category TEXT
        )''')

init_db()

@app.route("/add", methods=["POST"])
def add_expense():
    data = request.json
    desc = data["description"]
    amount = float(data["amount"])
    date = data.get("date", datetime.now().strftime("%Y-%m-%d"))

    # Predict category using AI
    X = vectorizer.transform([desc])
    category = model.predict(X)[0]

    with sqlite3.connect("expenses.db") as conn:
        conn.execute("INSERT INTO expenses (date, description, amount, category) VALUES (?, ?, ?, ?)",
                     (date, desc, amount, category))

    return jsonify({"message": "Expense added", "predicted_category": category})

@app.route("/expenses", methods=["GET"])
def get_expenses():
    with sqlite3.connect("expenses.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM expenses ORDER BY date DESC")
        rows = cur.fetchall()
        return jsonify(rows)

@app.route("/")
def home():
    return "<h2>💸 SmartExpense AI is running!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
