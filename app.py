from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# -------- CHATBOT LOGIC --------
def chatbot_response(user_input):
    msg = user_input.lower()

    if "hello" in msg:
        return "Hi! 👋 How can I help you?"
    
    elif "bmi" in msg:
        return "BMI = weight (kg) / height² (m²)"
    
    elif "calculate bmi" in msg:
        return "Please tell me your weight and height."
    
    elif "bye" in msg:
        return "Goodbye! Stay healthy 😊"

    else:
        return "Sorry, I didn't understand. Try asking about BMI."

# -------- ROUTES --------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    data = request.get_json()
    user_input = data["message"]
    reply = chatbot_response(user_input)
    return jsonify({"response": reply})

# -------- RUN SERVER --------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
