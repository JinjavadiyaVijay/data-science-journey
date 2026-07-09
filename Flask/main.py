from flask import Flask, render_template,url_for

app = Flask(__name__,static_folder = "assest")

@app.route("/")
def Hello():
    print(url_for("static",filename = "style.css"))
    return render_template("index.html")

@app.route("/login")
def prime():
    return render_template("login.html")

app.run(debug = True)

if __name__ == "__main__":
    app.run(debug = True)