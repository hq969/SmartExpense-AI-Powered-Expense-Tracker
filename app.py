from flask import Flask, render_template, request, jsonify
import sqlite3
import pickle
from datetime import datetime

app = Flask(__name__)

# Load AI model and vectorizer
with open('ai_model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('ai_model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Database init
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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        description = request.form["description"]
        amount = float(request.form["amount"])
        date = request.form.get("date") or datetime.now().strftime("%Y-%m-%d")

        X = vectorizer.transform([description])
        category = model.predict(X)[0]

        with sqlite3.connect("expenses.db") as conn:
            conn.execute("INSERT INTO expenses (date, description, amount, category) VALUES (?, ?, ?, ?)",
                         (date, description, amount, category))

        return render_template("index.html", success=True, category=category)

    # Show recent expenses
    with sqlite3.connect("expenses.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM expenses ORDER BY date DESC")
        expenses = cur.fetchall()

    return render_template("index.html", expenses=expenses)

@app.route("/api/expenses")
def api_expenses():
    with sqlite3.connect("expenses.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM expenses ORDER BY date DESC")
        return jsonify(cur.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
