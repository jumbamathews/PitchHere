from . import db
from . import login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash,check_password_hash



class User(UserMixin,db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'{self.username}'



class Pitch(db.Model):
    '''
    '''

    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.Text, index = True)
    downvotes = db.Column(db.Integer, default=int(0))
    upvotes = db.Column(db.Integer, default=int(0))
    category = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment',backref='pitch',lazy='dynamic')

def __repr__(self):
		return f'User {self.body}'



class Comment(db.Model):
	""" This model handles the Comment model that will be mapped to the database"""

	__tablename__='comments'
	id = db.Column(db.Integer,primary_key=True)
	body = db.Column(db.Text)
	owneer_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
	pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'),
        nullable=False)

	def __repr__(self):
		return f"Comment : id: {self.id} comment: {self.body}"



    