from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        fraud_type = request.form["fraud_type"]

        try:
            response = requests.post("http://127.0.0.1:8000/ai-guide", json={"fraud_type": fraud_type})
            data = response.json()
        except Exception as e:
            data = {"error": str(e)}

        return render_template("guidance.html", data=data)

    return render_template("report.html")
