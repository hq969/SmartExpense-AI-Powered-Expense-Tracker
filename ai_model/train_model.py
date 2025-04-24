import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample dataset
data = {
    'description': [
        'Bought groceries at supermarket',
        'Paid electricity bill',
        'Dinner at restaurant',
        'Monthly rent payment',
        'Internet recharge',
        'Gas station fuel',
        'Movie tickets',
        'Bus fare'
    ],
    'category': [
        'Food', 'Utilities', 'Food', 'Housing', 'Utilities', 'Transport', 'Entertainment', 'Transport'
    ]
}

df = pd.DataFrame(data)

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['description'])

# Model training
model = MultinomialNB()
model.fit(X, df['category'])

# Save model and vectorizer
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
