import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_model():
   data = [
    ("I feel anxious", "anxiety"),
    ("I have anxiety", "anxiety"),
    ("I am stressed and worried", "anxiety"),
    ("I can't relax", "anxiety"),

    ("I feel sad", "depression"),
    ("I am not happy", "depression"),
    ("I feel empty", "depression"),
    ("I lost interest in things", "depression"),

    ("How to stay healthy", "health"),
    ("Give me health tips", "health"),
    ("How to improve mental health", "health"),
    ("How to live a healthy life", "health")
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
    prob = model.predict_proba(X).max()

    # ✅ Confidence check
    if prob < 0.5:
        return "I'm not fully sure. Please consult a healthcare professional."

    # ✅ Extra keyword understanding
    if "sleep" in user_input:
        return "Good sleep (7–8 hours) is important for mental health."

    if "diet" in user_input or "food" in user_input:
        return "Eat a balanced diet with fruits and vegetables."

    if "exercise" in user_input:
        return "Regular exercise helps reduce stress."

    # ✅ Model-based response
    if pred == "anxiety":
        return "You may be experiencing anxiety. Try relaxation techniques."

    elif pred == "depression":
        return "This may be depression. Stay connected and seek help."

    else:
        return "Maintain good mental health with proper sleep and lifestyle."
