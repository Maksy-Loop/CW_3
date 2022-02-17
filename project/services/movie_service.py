from project.dao.movie import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas.movie import MovieSchema
from project.services.base import BaseService



class MoviesService(BaseService):
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_item_by_id(self, pk):
        director = self.dao.get_by_id(pk)
        if not director:
            raise ItemNotFound
        return MovieSchema().dump(director)

    def get_all_genres(self):
        director = self.dao.get_all()
        return MovieSchema(many=True).dump(director)
