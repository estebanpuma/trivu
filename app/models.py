from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
import math as ma


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    height = db.Column(db.Float)
    birth = db.Column(db.DateTime)
    weekdata = db.relationship('WeekData', backref='user', lazy='dynamic')

    def __repr__(self):
        return self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return  'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

class WeekData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float)
    neck = db.Column(db.Float)
    waist = db.Column(db.Float)
    body_fat = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Peso: {} Grasa corporal: {}'.format(self.weight, self.body_fat)

    def calc_body_fat(self):
        user = User.query.filter_by(id=self.user_id).first()
        self.body_fat = 86.01*ma.log10((self.waist/2.54)-(self.neck/2.54))-70.041*ma.log10(user.height/2.54)+36.76

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
