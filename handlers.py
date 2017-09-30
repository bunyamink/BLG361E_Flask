from flask import Blueprint, render_template
from datetime import datetime
from flask import current_app

site = Blueprint('site', __name__)

@site.route('/')
def home_page():
    now = datetime.now()
    day = now.strftime('%A')
    return render_template('home.html', day_name=day)


@site.route('/movies')
def movies_page():
	movies =  current_app.store.get_movies()
	return render_template('movies.html', movies=sorted(movies.items()))

@site.route('/movie/<int:movie_id>')
def movie_page(movie_id):
	movie = current_app.store.get_movie(movie_id)
	return render_template('movie.html', movie=movie)
