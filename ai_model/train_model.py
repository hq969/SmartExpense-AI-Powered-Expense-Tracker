import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample labeled data
data = {
    'description': [
        'Pizza from Domino’s', 'Uber ride to office', 'Paid monthly rent',
        'Groceries from Walmart', 'Electricity bill', 'Netflix subscription',
        'Bus ticket', 'Coffee from Starbucks'
    ],
    'category': [
        'Food', 'Transport', 'Rent',
        'Groceries', 'Utilities', 'Entertainment',
        'Transport', 'Food'
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['description'])
y = df['category']

model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
with open('ai_model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('ai_model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ AI model trained and saved.")
