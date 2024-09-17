from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Using SQLAlchemy to define the tables of the database

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String, nullable=False)

    movies = db.relationship('Movie', backref='user', lazy=True)
    '''
    This is the relationship between the tables of the database
    '''

    def __str__(self):
        return f"User name: {self.name}"

    def __repr__(self):
        return f"User id: {self.id} User name: {self.name}"


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    poster_url = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    '''
    the user_id is the foreign key of the table movies
    '''

    def __repr__(self):
        return f"Movie id: {self.id} Movie name:{self.name}"

    def __str__(self):
        return f"Movie name:{self.name} Movie's director: {self.director}"
