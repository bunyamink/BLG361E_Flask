class Store:
	def __init__(self):
		self.movies= {}
		self.last_movie_id = 0
	
	def add_movie(self, movie):
		self.last_movie_id += 1
		self.movies[self.last_movie_id] = movie
		movie._id = self.last_movie_id
	
	def delete_movie(self, movie_id):
		del self.movies[movie_id]

	def get_movie(self, movie_id):
		return self.movies[movie_id]
		
	def get_movies(self):
		return self.movies
