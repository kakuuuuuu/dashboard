"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.db = self._app.db
        if 'logstatus' not in session:
            session['logstatus']=False
    def index(self):
        return self.load_view('userpage.html')
    def adduser(self):
        user_info={
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':request.form['password'],
            'passconfirm':request.form['passconfirm']
        }
        create_status=self.models['User'].create_user(user_info)
        if create_status['status']==True:
            create_status.pop('status')
            if session['logstatus']==True:
                return redirect('/dashboard')
            else:
                session['logstatus']=True
                session['first_name']=create_status['user']['first_name']
                session['last_name']=create_status['user']['last_name']
                session['id']=create_status['user']['id']
                session['permission']=create_status['user']['permission']
                return redirect('/dashboard')
        else:
            for error in create_status['errors']:
                flash(error,"registration_error")
            if session['logstatus']==True:
                return redirect('/users/new')
            return redirect('/register')
    def updateinfo(self,user_id):
        if session['id']==user_id:
            user_info={
                'id':user_id,
                'email':request.form['email'],
                'first_name':request.form['first_name'],
                'last_name':request.form['last_name'],
                'description':request.form['description']
            }
        else:
            user_info={
                'id':user_id,
                'email':request.form['email'],
                'first_name':request.form['first_name'],
                'last_name':request.form['last_name'],
                'level':request.form['level']
            }
        check=self.models['User'].update_info(user_info,session['id'],session['permission'])
        if check['status']==False:
            for error in check['errors']:
                flash(error,"update_error")
                url='users/edit/'+str(user_id)
                return redirect(url)
        else:
            return redirect('/dashboard')
        # return redirect('/dashboard')

    def loginuser(self):
        user_info={
            'email':request.form['email'],
            'password':request.form['password']
        }
        check=self.models['User'].login_user(user_info)
        if check!=False:
            session['logstatus']=True
            session['first_name']=check['first_name']
            session['last_name']=check['last_name']
            session['id']=check['id']
            session['permission']=check['permission']
            return redirect('/dashboard')
        else:
            flash("Incorrect Password", "login_error")
            return redirect('/login')
    def logout(self):
        session['logstatus']=False
        session.pop('first_name')
        session.pop('last_name')
        session.pop('id')
        session.pop('permission')
        return redirect('/')
