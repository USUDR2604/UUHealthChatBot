import json
import pandas as pd
from preprocess import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle
import nltk
nltk.data.path.append('/Users/udaydeepreddy/Desktop/HealthCareSystem/venv/HealthCare/nltk_data/tokenizers/')
# Load intents data
with open("intents.json") as file:
    intents = json.load(file)

# Prepare data for training
data = []
for intent in intents['intents']:
    tag = intent['tag']
    for pattern in intent['patterns']:
        data.append({'tag': tag, 'pattern': preprocess_text(pattern)})
df = pd.DataFrame(data)

# Vectorize patterns and encode labels
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(df['pattern']).toarray()
encoder = LabelEncoder()
y = encoder.fit_transform(df['tag'])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model, vectorizer, and encoder
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
with open("encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)
