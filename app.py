from flask import Flask, request, render_template, jsonify
import os
import requests
from dotenv import load_dotenv
from faq import get_faq_answer

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("message")
<<<<<<< HEAD

     # Try to get a predefined FAQ answer
    answer = get_faq_answer(user_input)
    if answer:
        return jsonify({"response": answer})
        
    # Hugging Face Inference API
=======
    # Try to get a predefined FAQ answer
    answer = get_faq_answer(user_input)
    if answer:
        return jsonify({"response": answer})
    # AI Inference API
>>>>>>> 93aa967 (Initial commit)
    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {
        "inputs": f"Answer this IT support question: {user_input}"
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    print("MODEL RESPONSE:", result)

    try:
        answer = result[0]["generated_text"]
    except (KeyError, IndexError, TypeError):
        answer = "Sorry, something went wrong. Try again later."

    return jsonify({"response": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
