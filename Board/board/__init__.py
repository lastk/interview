from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
board_session_factory = UnencryptedCookieSessionFactoryConfig('rafboardsecret')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings,session_factory=board_session_factory)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.scan()
    return config.make_wsgi_app()
