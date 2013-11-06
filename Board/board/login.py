from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from user import User



@view_config(route_name='login', renderer="templates/login.pt")
def login_view(request):  
  session = request.session
  if 'user' in session:
    session.flash("you are already logged in.")
    return HTTPFound(location=request.route_url('home'))
    

  if request.method == "POST":
    user = User(request.POST.get("email"))
    if user.authenticate(request.POST.get("password")):
      session["user"] = user
      return HTTPFound(location=request.route_url('home'))
      
  return {'title': 'Login','session': session}
