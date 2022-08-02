from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "Logged in"


@auth.route("/logout")
def logout():
    return "Logged out"


@auth.route("/sign-up")
def sign_up():
    return "Signed up"
