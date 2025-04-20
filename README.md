# 💸 SmartExpense - AI Powered Expense Tracker

SmartExpense is an intelligent expense tracker powered by machine learning. It classifies your expenses automatically based on the description using a Natural Language Processing (NLP) model. Designed for simplicity, accuracy, and clarity, it helps users manage their finances smarter and faster.

---

## 🚀 Features

- 🧠 **AI-Powered Categorization**  
  Automatically categorizes expenses (e.g., food, rent, utilities) using a trained NLP classifier.

- 📝 **Intuitive Expense Logging**  
  Enter your expenses naturally like *"Uber ride"* or *"Netflix subscription"*—the AI figures out the rest.

- 📊 **Detailed Expense Dashboard**  
  View and analyze recent expenses categorized by date, type, and amount.

- 🛠️ **Lightweight and Fast**  
  Built using Python (Flask) and SQLite with an optional HTML/CSS frontend.

---

## 🧠 Tech Stack

| Layer       | Technology         |
|-------------|--------------------|
| Backend     | Python + Flask     |
| AI/ML       | Scikit-learn, NLP  |
| Frontend    | HTML, CSS (Bootstrap optional) |
| Database    | SQLite (can be upgraded to PostgreSQL/MySQL) |

---

## 📂 Project Structure

SmartExpense-AI/ 

│ ├── app.py # Flask app logic 

├── ai_model/ │ 

├── train_model.py # Trains the ML model │ 

├── model.pkl # Saved classifier model │ 

└── vectorizer.pkl # Saved TF-IDF vectorizer 

├── templates/ │ 

└── index.html # Frontend HTML 

├── static/ │ 

└── style.css # CSS styling 

├── requirements.txt # Python dependencies 

└── README.md # Project overview




---

## 🧪 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/hq969/SmartExpense-AI.git
cd SmartExpense-AI

pip install -r requirements.txt
python ai_model/train_model.py
python app.py

Open your browser and go to http://localhost:5000


📈 Sample Usage
POST Form:
Description: Bought pizza from Domino's

Amount: 450

➡️ Auto-classified as "Food"



🔐 Future Enhancements
📱 Add React-based responsive frontend

☁️ Deploy on Heroku/Docker/Render

📊 Add monthly analytics & charts

👥 User authentication for multi-user usage

🔔 Budget alerts and email notifications


🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

📃 License
This project is licensed under the MIT License.





