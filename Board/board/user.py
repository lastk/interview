class User(object):
    def __init__(self,login,password):
        self.login = login
        self.password = password

    def authenticate(self, password):
        return self.password == password
