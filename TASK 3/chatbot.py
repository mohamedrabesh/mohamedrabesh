import random
import json
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

with open("intents.json") as f:
    data = json.load(f)

def get_response(user_input):
    vec = vectorizer.transform([user_input])
    tag = model.predict(vec)[0]
    
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

print("CodBot is ready! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("CodBot: Goodbye!")
        break
    response = get_response(user_input)
    print("CodBot:", response)
