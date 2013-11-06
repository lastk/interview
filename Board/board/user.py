class User(object):
    def __init__(self,login):
        self.login = login
        self.password = "123123" #hardcoded password :)
    def authenticate(self, password):
        return self.password == password
