from api.factory import Factory
from api.config import Config
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('api').version
except pkg_resources.DistributionNotFound:
    __version__ = Config.VERSION


factory = Factory()
factory.set_flask()
factory.set_celery()

from api.resources import blueprint

factory.register(blueprint)