import pickle

model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

def generate_response(user_input):
    X = vectorizer.transform([user_input])
    pred = model.predict(X)[0]

    if pred == "anxiety":
        return "You may be experiencing anxiety. Try relaxation and consult a doctor."

    elif pred == "depression":
        return "This may be depression. Stay connected with people and seek help."

    else:
        return "Maintain good mental health with proper sleep, diet, and exercise."