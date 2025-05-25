from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/outro")
def outro():
    return render_template("outro.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


