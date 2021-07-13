from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "This is my first flask app"


@app.route("/index/")
def index_page():
    return "This is my home page"


@app.route("/about/")
def about_page():
    return "<body style=background-color:gray><h1>THIS IS MY ABOUT PAGE</h1></body>"


@app.route("/contact/")
def contact_page():
    return "<body style=background-color:yellow><h1>You Can Find My Contact Details Below</h1></body><br><p>Hope To Hear From You Soon<p>"


@app.route("/projects/")
def projects_page():
    return "<body style=background-color:yellow><h1>Have A Look At Some Of The Projects I Have Done!!</h1></body>"


if __name__ == "__main__":
    app.debug = True
    app.run()
