from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


@view_config(route_name='home', renderer='templates/home.pt')
def my_view(request):
  session = request.session
  if 'user' not in session:
    session.flash("You need sign in before.")
    return HTTPFound(location=request.route_url('login'))

  return {'title': 'Board','session':session}
