from flask_restx import abort, Namespace, Resource
from project.exceptions import ItemNotFound
from project.implemented import director_service

director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):
    @director_ns.response(200, "OK")
    def get(self):
        """Get all genres"""
        return director_service.get_all_genres()


@director_ns.route("/<int:director_id>")
class DirectorView(Resource):
    @director_ns.response(200, "OK")
    @director_ns.response(404, "Director not found")
    def get(self, director_id: int):

        try:
            return director_service.get_item_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Genre not found")
