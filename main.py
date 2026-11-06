from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


# Creating a basic website
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        u_in = request.form["input"]
        return redirect(url_for("result", u_in=u_in))
    elif request.method == "GET":
        return render_template("home.html")

@app.route("/<u_in>")
def result(u_in):
    print(u_in)
    if request.method == "POST":
        u_in = request.form["input"]
        return redirect(url_for("result", u_in=u_in))
    elif request.method == "GET":
        return render_template("home.html")


# Testing the server
app.run("127.0.0.1", 5000, debug=True)
