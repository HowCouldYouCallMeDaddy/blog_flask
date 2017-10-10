from werkzeug import generate_password_hash
from werkzeug import check_password_hash

class User(object):
    def __init__(self):
        self.password_hash=''


    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)



if __name__ == '__main__':
    user = User()
    user.password('zeng')
    print user.verify_password('zeng')