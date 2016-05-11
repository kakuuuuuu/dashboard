"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class home(Controller):
    def __init__(self, action):
        super(home, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')
    def login(self):
        return self.load_view('users/login.html')
    def register(self):
        return self.load_view('users/register.html')
