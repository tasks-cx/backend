from flask import Blueprint, render_template

home_view = Blueprint("home_view", __name__,
                      static_folder='public', static_url_path='/static')

@home_view.route("/", methods=["GET"])
def home():
    return render_template("home/home.j2")
