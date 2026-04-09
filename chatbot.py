import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_model():
    data = [
        ("I feel anxious", "anxiety"),
        ("I am stressed", "anxiety"),
        ("I feel sad", "depression"),
        ("I am not happy", "depression"),
        ("How to stay healthy", "health")
    ]

    df = pd.DataFrame(data, columns=["text", "label"])

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["text"])

    model = LogisticRegression()
    model.fit(X, df["label"])

    return model, vectorizer

model, vectorizer = train_model()

def generate_response(user_input):
    user_input = user_input.lower()

    X = vectorizer.transform([user_input])
    pred = model.predict(X)[0]

    if pred == "anxiety":
        return "You may be experiencing anxiety. Try relaxation techniques."

    elif pred == "depression":
        return "This may be depression. Stay connected and seek help."

    else:
        return "Maintain good mental health with proper lifestyle."
