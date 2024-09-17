from data_manager.data_manager_interface import DataManagerInterface
from data_manager.data_models import db, Movie, User


class SQLiteDataManager(DataManagerInterface):
    '''
    This class is to use the methods to interact directly with the database,
    Creating all methods to modify the database to use after in the application
    '''
    def __init__(self, app):
        #creating the object using the flask app as a parameter
        self.app = app
        db.init_app(self.app)  # initializing the database when object is created
        '''
        with self.app.app_context(): 
            db.create_all() # creating the database for first time, then is not necessary
        '''

    def get_all_users(self):
        with self.app.app_context():  # ensure the database operations always work inside application context
            users = User.query.all()
            users_list = [user for user in users]
            return users_list

    def get_movies_user(self, user_id):  # getting a list of movies from specific user
        with self.app.app_context():
            movies = Movie.query.all()
            user_movies = [movie for movie in movies if movie.user_id == user_id]
            return user_movies

    def add_user(self, user_name):
        with self.app.app_context():
            new_user = User(name=user_name)
            db.session.add(new_user)
            db.session.commit()
            print("New user has been added")

    def add_movie(self, movie_name, director_name, year, rating, poster_url, user_id):
        with self.app.app_context():
            new_movie = Movie(
                name=movie_name,
                director=director_name,
                year=year,
                rating=rating,
                poster_url=poster_url,
                user_id=user_id
            )
            db.session.add(new_movie)
            db.session.commit()
            print("New Movie added")

    def update_movie(self, movie_id, director_name, year, rating):
        with self.app.app_context():
            movie = Movie.query.filter_by(id=movie_id).first()

            if movie:
                movie.director = director_name
                movie.year = year
                movie.rating = rating

            db.session.commit()
            print("Movie updated")

    def delete_movie(self, movie_id):
        with self.app.app_context():
            movie_to_delete = Movie.query.filter_by(id=movie_id).first()
            db.session.delete(movie_to_delete)
            db.session.commit()
            print("Movie deleted")

    def delete_user(self, user_id):
        with self.app.app_context():
            user_to_delete = User.query.filter_by(id=user_id).first()

            db.session.delete(user_to_delete)
            db.session.commit()
            print("User deleted")

    def get_movie_by_id(self, movie_id):
        with self.app.app_context():
            movie = Movie.query.filter_by(id=movie_id).first()
            return movie

