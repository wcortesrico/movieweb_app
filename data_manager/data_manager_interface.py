from abc import ABC, abstractmethod


class DataManagerInterface(ABC):
    '''
    With the abstract object, is to create the most important methods for the app
    '''

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_movies_user(self, user_id):
        pass

    @abstractmethod
    def add_user(self, user_name):
        pass

    @abstractmethod
    def add_movie(self, movie_name, director_name, year, rating, poster_url, user_id):
        pass
