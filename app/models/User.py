from system.core.model import Model
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def show_all_users(self):
        query="SELECT * FROM users"
        return self.db.query_db(query)
    def show_user(self,info):
        print info
        query="SELECT * FROM users WHERE id=:id LIMIT 1"
        data={'id':info}
        return self.db.query_db(query,data)[0]
    def login_user(self,info):
        query="SELECT * FROM users WHERE email=:email LIMIT 1"
        data={'email':info['email']}
        user=self.db.query_db(query,data)[0]
        if user:
            if self.bcrypt.check_password_hash(user['password'], info['password']):
                return user
        return False
    def update_info(self,info,editor_id,editor_permission):
        errors=[]
        if len(info['first_name'])<2 or len(info['last_name'])<2:
            errors.append('First and/or Last name cannot be less than 2 characters')
        if len(info['email'])<1:
            errors.append('Email field cannot be empty')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Did not enter a valid email')
        check_query="SELECT email FROM users WHERE id!=:id"
        checkdata={'id':info['id']}
        emails=self.db.query_db(check_query,checkdata)
        for email in emails:
            if email['email']==info['email']:
                errors.append('Email already exists in another account')
        permquery="SELECT permission FROM users WHERE id=:id"
        permdata={'id':info['id']}
        if editor_id!=info['id'] and editor_permission<self.db.query_db(permquery,permdata)[0]['permission']:
            errors.append('Cannot edit the permissions for this user')
        if errors:
            return {"status": False, "errors":errors}
        else:
            if editor_id==info['id']:
                query="UPDATE users SET first_name=:first_name,last_name=:last_name,email=:email,description=:description WHERE id=:id"
                data={'id':info['id'],'first_name':info['first_name'],'last_name':info['last_name'],'email':info['email'],'description':info['description']}
            else:
                if info['level']=='normal':
                    level=1
                else:
                    level=8
                query="UPDATE users SET first_name=:first_name,last_name=:last_name,email=:email,permission=:permission WHERE id=:id"
                data={'id':info['id'],'first_name':info['first_name'],'last_name':info['last_name'],'email':info['email'],'permission':level}
            self.db.query_db(query,data)
            return {"status":True}

    def destroy_user(self,user_id,permission):
        check=self.db.query_db("SELECT permission FROM users WHERE id=:id", {'id':user_id})[0]
        if permission>check['permission']:
            query="DELETE FROM users WHERE id=:id"
            data={'id':user_id}
            self.db.query_db(query,data)
            return {'status':True}
        else:
            error='You cannot delete this user'
            return {'status':False,'error':error}
    def create_user(self,info):
        errors=[]
        if len(info['first_name'])<2 or len(info['last_name'])<2:
            errors.append('First and/or Last name cannot be less than 2 characters')
        if len(info['email'])<1:
            errors.append('Email field cannot be empty')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Did not enter a valid email')
        if len(info['password'])<1:
            errors.append('Password field cannot be empty')
        elif len(info['password'])>8:
            errors.append('Password cannot be longer than 8 characters')
        elif info['password']!=info['passconfirm']:
            errors.append('Password does not match confirmation')
        check_query="SELECT email FROM users WHERE email=:email"
        checkdata={'email':info['email']}
        if len(self.db.query_db(check_query,checkdata))!=0:
            errors.append('Account with this email already exists')
        if errors:
            return {"status": False, "errors":errors}
        else:
            add_query="INSERT INTO users (first_name,last_name,email,password,permission,created_at,updated_at) VALUES (:first_name,:last_name,:email,:password,:permission,NOW(),NOW())"
            data={
                'first_name':info['first_name'],
                'last_name':info['last_name'],
                'email':info['email'],
                'password':self.bcrypt.generate_password_hash(info['password']),
                'permission':0
            }
            query="SELECT id FROM users"
            if len(self.db.query_db(query))==0:
                data['permission']=9
            else:
                data['permission']=1
            self.db.query_db(add_query,data)
            user_query="SELECT * FROM users WHERE email=:email"
            user=self.db.query_db(user_query,data)[0]
            print user
            return {"status": True, "user":user}
