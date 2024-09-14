from flask_sqlalchemy import SQLAlchemy
from data_manager_interface import DataManagerInterface
from data_models import db, User, Movie
from flask import Flask

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.app = Flask(__name__) # creating the flask app
        self.app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{db_file_name}'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
        self.db = SQLAlchemy(self.app) # initialize SQLAlchemy with the flask app

    def get_all_users(self):
        users = User.query.all()
        users_list = [user for user in users]
        return users_list
    def get_movies_user(self, user_id):
        movies = Movie.query.all()
        user_movies = [movie for movie in movies if movie.user_id == user_id]
        return user_movies

    def add_user(self, user_name):
        new_user = User(name=user_name)

        self.db.session.add(new_user)
        self.db.session.commit()
        print("New user has been added")

    def add_movie(self, movie_name, director_name, year, rating, user_id):
        new_movie = Movie(
            name=movie_name,
            director=director_name,
            year=year,
            rating=rating,
            user_id=user_id
        )

        self.db.session.add(new_movie)
        self.db.session.commit()
        print("New Movie added")

    def update_movie(self, movie_id, new_director_name, new_year, new_rating):
        movie = Movie.query.filter_by(id=movie_id).first()

        if movie:
            movie.director = new_director_name
            movie.year = new_year
            movie.rating = new_rating

        self.db.session.commit()
        print("Movie updated")

    def delete_movie(self, movie_id):
        movie_to_delete = Movie.query.filter_by(id=movie_id).first()

        self.db.session.delete(movie_to_delete)
        self.db.session.commit()


