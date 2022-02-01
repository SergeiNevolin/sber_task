from flask import Blueprint
from flask_restful import Api
from api.config import Config
from api.resources.main import Tags, TagsStatus

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint)

api.add_resource(Tags, '/tags')
api.add_resource(TagsStatus, '/tags/<id>')