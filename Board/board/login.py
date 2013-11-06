from pyramid.view import view_config

@view_config(route_name='login', renderer="templates/login.pt")
def login_view(request):
    if 'submit' in request.POST:
        pass
    return {'title': 'Login'}
