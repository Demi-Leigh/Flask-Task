from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/user/<name>")
def user_page(name):
    if name == "Demi":
        return redirect(url_for('admin_page', name=name))
    else:
        return redirect(url_for('guest_page', name=name))


@app.route("/guest/<name>")
def guest_page(name):
    return "I am a guest. My name is %s" % name


@app.route("/admin/<name
def admin_page(name):
    return "The admin is %s" % name


if __name__ == "__main__":
    app.debug = True
    app.run()
