from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/law-guide")
def law_guide():
    try:
        # Call FastAPI backend
        response = requests.get("http://127.0.0.1:8000")
        data = response.json()
    except Exception as e:
        data = {"message": f"Error connecting to backend: {str(e)}"}
    
    return render_template("law_guide.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
