from flask_restx import Resource, Namespace
from flask import request
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):

    def post(self):
        user_d = request.json
        user_service.create(user_d)

        return "Done", 200
