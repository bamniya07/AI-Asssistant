# app.py
from flask import Flask, request, jsonify
from jarvis_core import process_query

app = Flask(__name__)

@app.route('/')
def home():
    return "🧠 JARVIS API is running!"

@app.route('/ask', methods=['POST'])
def ask_jarvis():
    data = request.get_json()
    query = data.get("query")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    response = process_query(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
