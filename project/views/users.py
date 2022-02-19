from flask_restx import Resource, Namespace
from flask import request
from project.implemented import user_service

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):

    def get(self):
        pass


    def put(self):
        user_d = request.json
        user_service.create(user_d)

        pass

    def patch(self):
        pass


