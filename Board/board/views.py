from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from boardData import BoardData


@view_config(route_name='home', renderer='templates/home.pt')
def my_view(request):
  session = request.session
  if 'user' not in session:
    session.flash("You need sign in before.")
    return HTTPFound(location=request.route_url('login'))

  #if you want to load a little data before :)
  #data = BoardData(request)
  #data.seed()

  messages = request.db['board'].find()

  _messages = []
  for m in messages:
    _messages.append(m)

  
  return {'title': 'Board','session':session, 'messages': _messages}
