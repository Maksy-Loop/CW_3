from project.dao.genre import GenreDAO
from project.dao.director import DirectorDAO
from project.dao.movie import MovieDAO

from project.services.genres_service import GenresService
from project.services.director_service import DirectorsService
from project.services.movie_service import MoviesService

from project.setup_db import db

genre_dao = GenreDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)


director_service = DirectorsService(dao=director_dao)
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
