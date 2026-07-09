from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello():
    return "<p> Hello world! <p>"

@app.route("/prime")
def prime():
    return "<p>Have a Good day<P>"

app.run(debug = True)

if __name__ == "__main__":
    app.run(debug = True)