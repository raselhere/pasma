from flask import Flask, request, jsonify

app = Flask(__name__)

responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a great day!",
    "what is your name": "I'm PASMA AI Chatbot, here to help you.",
    "default": "I'm not sure about that. Can you rephrase?"
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()  # Get JSON from frontend
    user_message = data.get("message", "").lower()  # Get user input
    print(f"User: {user_message}")  # Debugging print

    response = responses.get(user_message, responses["default"])
    print(f"Bot: {response}")  # Debugging print

    return jsonify({"response": response})  # Send JSON response

if __name__ == "__main__":
    app.run(debug=True)
