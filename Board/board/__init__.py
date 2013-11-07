from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
board_session_factory = UnencryptedCookieSessionFactoryConfig('rafboardsecret')

from urlparse import urlparse
import pymongo


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings,session_factory=board_session_factory)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = pymongo.Connection()

    def add_db(request):
      db = config.registry.db[db_url.path[1:]]
      db.authenticate
      return db


    config.add_request_method(add_db, 'db', reify= True)
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('show', '/show/{id}')
    config.scan()
    return config.make_wsgi_app()
