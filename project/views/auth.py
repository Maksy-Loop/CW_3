from flask_restx import Resource, Namespace
from flask import jsonify, make_response, request
from dao.model.user import UserSchema
from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):

    def post(self):
        data = request.json
        tokens = auth_service.create_tokens(data)

        return make_response(jsonify(tokens), 201)

    def put(self):
        data = request.json
        tokens = auth_service.create_tokens_with_rt(data)

        return make_response(jsonify(tokens), 201)





