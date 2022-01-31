from flask_restful import Resource
from flask import request,jsonify
from logic.LogicEvento import *

class ResourceEventos(Resource):
    def post(self):
        return jsonify(createEvento(request.json))
class ResourceEvento(Resource):
    def get(self,id):
        return jsonify(findEvento(id))
    def put(self,id):
        return updateEvento(id,request.json)
    def delete(self,id):
        return deleteEvento(id)
class ResourceUserEventos(Resource):
    def get(self,id):
        return findUserEventos(id)