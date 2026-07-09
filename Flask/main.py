from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Hello():
    return render_template("index.html")

@app.route("/login")
def prime():
    return render_template("login.html")

app.run(debug = True)

if __name__ == "__main__":
    app.run(debug = True)