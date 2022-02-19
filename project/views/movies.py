from flask_restx import abort, Namespace, Resource
from project.exceptions import ItemNotFound
from project.implemented import movie_service
from flask import request

movie_ns = Namespace("movies")


@movie_ns.route("/")
class MoviesView(Resource):
    @movie_ns.response(200, "OK")
    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")
        filters = {
            "status": status,
            "page": page
        }
        """Get all genres"""
        return movie_service.get_all(filters)


@movie_ns.route("/<int:id>")
class MovieView(Resource):
    @movie_ns.response(200, "OK")
    @movie_ns.response(404, "Director not found")
    def get(self, id: int):

        try:
            return movie_service.get_item_by_id(id)
        except ItemNotFound:
            abort(404, message="Genre not found")
