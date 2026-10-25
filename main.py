import flask


app = flask.Flask(__name__)


# Creating a basic website
@app.route("/")
def homePage():
    return flask.render_template("home.html")


@app.route("/get_deff/<input>")
def getDeff(input: str):
    print(input)
    return input


# Testing the server
app.run("127.0.0.1", 5000, debug=True)
