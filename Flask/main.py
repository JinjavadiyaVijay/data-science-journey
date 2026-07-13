from flask import Flask, render_template,url_for,request,jsonify

app = Flask(__name__,static_folder = "assest")

@app.route("/")
def Hello():
    
    data ={
        "message": "welcome to the platform!"
    }
    return render_template("index.html",name=name,sub = subject)

@app.route("/login",methods = ["GET","POST"])
def prime():
    return render_template("login.html")

@app.route("/login-handle",methods = ["GET","POST"])
def login_handle():
    if request.method == "POST":
        print(request.form)
        name = request.form["username"]
        password = request.form["password"]

    return f"<p> Welcome {name}!</p>"

app.run(debug = True)

if __name__ == "__main__":
    app.run(debug = True)
