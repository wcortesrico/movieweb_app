from data_manager.sqlite_data_manager import SQLiteDataManager
from flask import render_template, Flask

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movieweb_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
data_manager = SQLiteDataManager(app)


@app.route('/')
def home():
    return "Welcome to your movie app"


@app.route('/users')
def list_users():
    users = data_manager.get_all_users()

    return render_template('users.html', users=users)


@app.route('/users/<user_id>')
def user_movies(user_id):
    pass


@app.route('/add_user')
def add_user():
    pass


@app.route('/add_movie')
def add_movie():
    pass


@app.route('/users/<user_id>/update_movie/<movie_id>')
def update_movie(user_id, movie_id):
    pass


@app.route('/users/<user_id>/delete_movie/<movie_id>')
def delete_movie(user_id, movie_id):
    pass


if __name__ == "__main__":
    app.run(debug=True)
