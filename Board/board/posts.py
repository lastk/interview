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

  id   = request.matchdict['id']
  data = BoardData(request)

  if request.method == "POST":
    data.update(id,request.POST.get("message"))
  
  post    = data.find(id)
  
  return {'title':'View','session':session, 'post': post}


@view_config(route_name='new', renderer="templates/new.pt")
def new(request):
  session = request.session
  if 'user' not in session:
    session.flash("You need sign in before.")
    return HTTPFound(location=request.route_url('login'))  

  if request.method == "GET":
    return {'title':'New','session':session}

  if request.method == "POST":
    user = session['user']
    #def insert(self,user_name, title, message):
    data = BoardData(request)
    data.insert(user.login, request.POST.get("title"), request.POST.get("message"))
    return HTTPFound(location=request.route_url('home'))


  