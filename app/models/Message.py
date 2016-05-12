"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()
    def create_message(self,info):
        query = "INSERT INTO messages (user_id, posted_id, message, created_at, updated_at) VALUES(:user_id,:posted_id, :message, NOW(), NOW())"
        data = {'user_id': info['user_id'],'posted_id':info['posted_id'], 'message': info['message']}
        self.db.query_db(query,data)
    def show_all_messages(self,user_id):
        query="SELECT message,user_id,messages.id,messages.created_at as postedon,first_name,last_name FROM messages JOIN users ON messages.user_id=users.id WHERE posted_id=:user_id"
        data={'user_id':user_id}
        return self.db.query_db(query,data)
    def create_comment(self,info):
        query = "INSERT INTO comments (user_id, posted_id, message_id, comment, created_at, updated_at) VALUES(:user_id,:posted_id,:message_id, :comment, NOW(), NOW())"
        data = {'user_id': info['user_id'],'posted_id':info['posted_id'],'message_id':info['message_id'], 'comment': info['comment']}
        self.db.query_db(query,data)
    def show_all_comments(self,user_id):
        query="SELECT comments.id,comment,message_id,user_id,comments.created_at as postedon,first_name,last_name FROM comments JOIN users ON comments.user_id=users.id WHERE posted_id=:user_id"
        data={'user_id':user_id}
        return self.db.query_db(query,data)
