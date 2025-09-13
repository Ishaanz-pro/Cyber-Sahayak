from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/law-guide")
def law_guide():
    return "<h2>Cyber Law Guide will come here soon 🚀</h2>"

if __name__ == "__main__":
    app.run(debug=True)

