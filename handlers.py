from flask import Blueprint, render_template, redirect, url_for
from datetime import datetime
from flask import current_app, request
from movie import Movie

site = Blueprint('site', __name__)

@site.route('/')
def home_page():
    now = datetime.now()
    day = now.strftime('%A')
    return render_template('home.html', day_name=day)


@site.route('/movies', methods=['GET', 'POST'])
def movies_page():
	if request.method == 'GET':
		movies = current_app.store.get_movies()
		return render_template('movies.html', movies=sorted(movies.items()))
	else:
		movie_ids = request.form.getlist('movie_ids')
		for movie_id in movie_ids:
			current_app.store.delete_movie(int(movie_id))
		return redirect(url_for('site.movies_page'))

@site.route('/movie/<int:movie_id>')
def movie_page(movie_id):
	movie = current_app.store.get_movie(movie_id)
	return render_template('movie.html', movie=movie)
	
@site.route('/movies/add', methods=['GET', 'POST'])
def movie_add_page():
	if request.method == 'GET':
		form = {'title': '', 'year': ''}
	else:
		valid = validate_movie_data(request.form)
		if valid:
			title = request.form.data['title']
			year = request.form.data['year']
			movie = Movie(title, year=year)
			current_app.store.add_movie(movie)
			return redirect(url_for('site.movie_page', movie_id=movie._id))
		form = request.form
	return render_template('movie_edit.html', form=form, min_year=1887, max_year=datetime.now().year)
	
@site.route('/movie/<int:movie_id>/edit', methods=['GET', 'POST'])
def movie_edit_page(movie_id):
	movie = current_app.store.get_movie(movie_id)
	if request.method == 'GET':
		form = {'title': movie.title, 'year': movie.year if movie.year else ''}
		return render_template('movie_edit.html', form=form, min_year=1887, max_year=datetime.now().year)
	else:
		movie.title = request.form['title']
		movie.year = int(request.form['year']) if request.form['year'] else None
		current_app.store.update_movie(movie)
		return redirect(url_for('site.movie_page', movie_id=movie._id))

def validate_movie_data(form):
	form.data = {}
	form.errors = {}

	if len(form['title'].strip()) == 0:
		form.errors['title'] = 'Title can not be blank.'
	else:
		form.data['title'] = form['title']

	if not form['year']:
		form.data['year'] = None
	elif not form['year'].isdigit():
		form.errors['year'] = 'Year must consist of digits only.'
	else:
		year = int(form['year'])
		if (year < 1887) or (year > datetime.now().year):
			form.errors['year'] = 'Year not in valid range.'
		else:
			form.data['year'] = year

	return len(form.errors) == 0
