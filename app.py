from data_manager.sqlite_data_manager import SQLiteDataManager
from flask import render_template, Flask, request, redirect, url_for
from data_fetcher import fetch_data

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movieweb_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
data_manager = SQLiteDataManager(app)  # Creating the main object that will manage all querys from database


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/users')
def list_users():
    users = data_manager.get_all_users()

    return render_template('users.html', users=users)


@app.route('/users/<user_id>')
def user_movies(user_id):
    movies = data_manager.get_movies_user(int(user_id))

    return render_template('user_movies.html', movies=movies, user=user_id)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user_name = request.form['name']
        data_manager.add_user(user_name)
        return redirect(url_for('list_users'))
    return render_template('add_user.html')


@app.route('/users/<user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id):
    movies = data_manager.get_movies_user(user_id)
    if request.method == 'POST':
        movie_name = request.form['movie']
        movie_data = fetch_data(movie_name)
        title = movie_data['Title']
        director = movie_data['Director']
        year = movie_data['Year']
        rating = movie_data['imdbRating']
        poster = movie_data['Poster']
        data_manager.add_movie(movie_name=title, director_name=director, year=year,
                               rating=rating, poster_url=poster, user_id=user_id)
        return redirect(url_for('user_movies', movies=movies, user_id=user_id))
    return render_template('add_movie.html', user=user_id)


@app.route('/users/<user_id>/update_movie/<movie_id>', methods=['GET', 'POST'])
def update_movie(user_id, movie_id):
    movie = data_manager.get_movie_by_id(movie_id)
    if request.method == 'POST':
        new_director = request.form.get('director')
        new_year = request.form.get('year')
        new_rating = request.form.get('rating')
        data_manager.update_movie(movie_id=movie_id, director_name=new_director, year=new_year, rating=new_rating)
        return redirect(url_for('user_movies', user_id=user_id))
    return render_template('update_movie.html', movie=movie)


@app.route('/users/<user_id>/delete_movie/<movie_id>', methods=['GET', 'POST'])
def delete_movie(user_id, movie_id):
    movie = data_manager.get_movie_by_id(movie_id)
    movies = data_manager.get_movies_user(user_id)
    print(movie_id)
    print(user_id)
    if request.method == 'POST':
        data_manager.delete_movie(movie_id)
        return redirect(url_for('user_movies', movies=movies, user_id=user_id))
    return render_template('delete_movie.html', movie=movie)


if __name__ == "__main__":
    app.run(debug=True)
