from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from user import User
from boardData import BoardData



@view_config(route_name='show', renderer="templates/show.pt")
def show(request):  
  session = request.session
  if 'user' not in session:
    session.flash("You need sign in before.")
    return HTTPFound(location=request.route_url('login'))


  data = BoardData(request)
  
  id      = request.matchdict['id']
  post    = data.find(id)
  
  return {'title':'View','session':session, 'post': post}
  