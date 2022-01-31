from flask_restful import Resource
from flask import request
from logic.LogicUser import *

class ResourceUsers(Resource):
    def post(self):
        return createUser(request.json)
class ResourceUser(Resource):
    def put(self,id):
        return updateUser(id,request.json)
    def delete(self,id):
        return deleteUser(id)
class ResourceLogin(Resource):
    def post(self):
        return login(request.json)