from flask_restx import abort, Namespace, Resource
from project.exceptions import ItemNotFound
from project.implemented import movie_service

movie_ns = Namespace("movies")


@movie_ns.route("/")
class DirectorsView(Resource):
    @movie_ns.response(200, "OK")
    def get(self):
        """Get all genres"""
        return movie_service.get_all_genres()


@movie_ns.route("/<int:id>")
class DirectorView(Resource):
    @movie_ns.response(200, "OK")
    @movie_ns.response(404, "Director not found")
    def get(self, id: int):

        try:
            return movie_service.get_item_by_id(id)
        except ItemNotFound:
            abort(404, message="Genre not found")
