# app/main.py
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.db import post_db

bp = Blueprint('main', __name__)

@bp.route("/")
def main_page():
    return render_template("home.html")