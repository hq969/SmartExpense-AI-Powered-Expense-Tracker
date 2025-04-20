import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# Create the ai_model folder if not exists
os.makedirs("ai_model", exist_ok=True)

# Sample labeled data
data = {
    'description': [
        'Pizza from Domino’s', 'Uber ride to office', 'Paid monthly rent',
        'Groceries from Walmart', 'Electricity bill payment', 'Netflix subscription fee',
        'Bus ticket', 'Coffee from Starbucks', 'Mobile recharge',
        'Flight booking', 'New headphones purchase', 'Movie night with friends'
    ],
    'category': [
        'Food', 'Transport', 'Rent',
        'Groceries', 'Utilities', 'Entertainment',
        'Transport', 'Food', 'Utilities',
        'Transport', 'Shopping', 'Entertainment'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Step 1: Vectorize text data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['description'])

# Step 2: Train model
y = df['category']
model = MultinomialNB()
model.fit(X, y)

# Step 3: Save model and vectorizer
with open('ai_model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('ai_model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ AI model and vectorizer trained and saved in 'ai_model/'")
