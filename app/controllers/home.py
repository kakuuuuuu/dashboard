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
        if session['logstatus']==True:
            return redirect('/dashboard')
        return self.load_view('users/login.html')
    def register(self):
        if session['logstatus']==True:
            return redirect('/dashboard')
        return self.load_view('users/register.html')
    def adminadd(self):
        return self.load_view('users/register.html')
    def edit(self,user_id):
        if session['permission']>=8 or session['id']==user_id:
            return self.load_view('users/edit.html',user_id=user_id)
        return redirect('/dashboard')
    def dashboard(self):
        if session['logstatus']==False:
            return redirect('/')
        users=self.models['User'].show_all_users()
        return self.load_view('dashboard.html',users=users)
    def userpage(self,user_id):
        print"here"
        user=self.models['User'].show_user(user_id)
        return self.load_view('users/userpage.html',user=user)
