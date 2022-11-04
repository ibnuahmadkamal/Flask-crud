from flask import Blueprint
from flask_restx import Api
from app.api.user.routes import api as user_api
from app import app

# add blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(
    api_bp,
    description='webhook blueprint',
    doc='/doc'
)

api.add_namespace(user_api)
