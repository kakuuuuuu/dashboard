"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)
        self.load_model('Message')
        self.db = self._app.db
    def addmsg(self,user_id):
        info={
            'user_id':session['id'],
            'message':request.form['message'],
            'posted_id':int(user_id)
        }
        self.models['Message'].create_message(info)
        url='/users/show/'+str(user_id)
        return redirect(url)
    def addcmt(self,user_id,message_id):
        print user_id, message_id
        info={
            'user_id':session['id'],
            'comment':request.form['comment'],
            'posted_id':int(user_id),
            'message_id':int(message_id)
        }
        self.models['Message'].create_comment(info)
        url='/users/show/'+str(user_id)
        return redirect(url)
    def deletemsg(self,user_id,message_id):
        self.models['Message'].delete_message(message_id)
        url='/users/show/'+str(user_id)
        return redirect(url)

    def deletecmt(self,user_id,comment_id):
        self.models['Message'].delete_comment(comment_id)
        url='/users/show/'+str(user_id)
        return redirect(url)
