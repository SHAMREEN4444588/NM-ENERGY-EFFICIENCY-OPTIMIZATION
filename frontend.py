from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Sample energy-saving tips
energy_tips = [
    "Turn off unused lights and appliances.",
    "Use energy-efficient LED bulbs.",
    "Optimize heating and cooling systems.",
    "Unplug electronics when not in use.",
    "Use smart thermostats to reduce energy consumption."
]

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").lower()
    
    if "energy" in user_message or "save" in user_message:
        response = random.choice(energy_tips)
    else:
        response = "EcoBot is here to help! Ask me about energy-saving tips."
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)