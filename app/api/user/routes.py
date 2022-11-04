from app import app
from flask import request
from flask_restx import Namespace, Resource, fields
import app.api.user.controllers as user_controller

api = Namespace('Users', description='Manage for create, read, update, delete user')

user_model = api.model('user_model', {
    'name': fields.String(required=True, description='User name'),
    'score': fields.Integer(required=True, description='User score start from 1-10')
})

@api.route('')
class CreateUser(Resource):
    @api.doc('Create User')
    @api.expect(user_model, validate=True)
    def post(self):
        payload = request.json
            
        try:
            resp = user_controller.create(payload)
            return {
                'msg': 'Data Created.',
                'user_id': resp
            }, 200
        except Exception as e:
            return e

@api.route('/<user_id>')
class GetDeleteUpdateUser(Resource):
    @api.doc('Get User')
    def get(self,user_id):
            
        try:
            resp = user_controller.get_user_by_id(user_id)
            return resp, 200
        except Exception as e:
            return e

    @api.doc('Update User')
    @api.expect(user_model, validate=True)
    def put(self,user_id):
        payload = request.json
            
        try:
            user_controller.update(payload,user_id)
            return {
                'msg': 'Data Updated.',
                'user_id': user_id
            }, 200
        except Exception as e:
            return e

    @api.doc('Delete User')
    def delete(self,user_id):
        try:
            user_controller.delete(user_id)
            return {
                'msg': 'Data Removed.',
                'user_id': user_id
            }, 200
        except Exception as e:
            return e