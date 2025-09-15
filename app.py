from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        # Call FastAPI backend
        response = requests.get("http://127.0.0.1:8000")
        backend_message = response.json().get("message", "No message from backend")
    except Exception as e:
        backend_message = f"Error connecting to backend: {e}"
    
    return f"""
    <h1>Cyber Law Guide 🚀</h1>
    <p>Backend says: {backend_message}</p>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)

