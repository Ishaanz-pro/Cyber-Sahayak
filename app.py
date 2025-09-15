from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/law-guide")
def law_guide():
    response = requests.get("http://127.0.0.1:8000")
    data = response.json()
    return render_template("law_guide.html", data=data)

@app.route("/report", methods=["GET", "POST"])
def report():
    guidance = None
    if request.method == "POST":
        category = request.form.get("category")
        response = requests.get(f"http://127.0.0.1:8000/guidance/{category}")
        guidance = response.json()["guidance"]
    return render_template("report.html", guidance=guidance)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
