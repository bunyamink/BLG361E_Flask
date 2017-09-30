from flask import Blueprint, render_template
from datetime import datetime


site = Blueprint('site', __name__)


@site.route('/')
def home_page():
    now = datetime.now()
    day = now.strftime('%A')
    return render_template('home.html', day_name=day)


@site.route('/movies')
def movies_page():
    return render_template('movies.html')
