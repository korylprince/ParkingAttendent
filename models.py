from flask import Flask
from sqlalchemy import Column, Integer, Unicode, DateTime, PickleType
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declared_attr
import flask.ext.sqlalchemy
from passlib.hash import sha512_crypt
from ParkingAttendent import app

# Create base class with default table name and id
class Base(flask.ext.sqlalchemy.Model):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)

# Overwrite default model
flask.ext.sqlalchemy.Model = Base
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):

    username = Column(Unicode(50), unique=True, nullable=False, index=True)
    name = Column(Unicode(100), nullable=False)
    pwhash = Column(Unicode(250), nullable=False)
    settings = Column(PickleType)

    @property
    def favorites(self):
        try:
            return self.settings.get('favorites',[])
        except AttributeError:
            return []

    def login(self, passwd):
        return sha512_crypt.verify(passwd, self.pwhash)

    def __repr__(self):
        return '<User({0})>'.format(self.username)

class Badge(db.Model):

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True)
    description = Column(Unicode(100), nullable=False, index=True)
    date = Column(DateTime, nullable=False, index=True)

    user = db.relationship('User', backref=db.backref('badges', order_by='Badge.date'))

    def __repr__(self):
        return '<Badge({0}, {1})>'.format(self.user, self.name)

class Lot(db.Model):

    description = Column(Unicode(250), nullable=False)

    @property
    def score(self):
        score = int(round(float(sum([x.score for x in self.checkins]))/len(self.checkins)))
        date = self.checkins[0].date
        users = set([x.user for x in self.checkins])
        return self.score_to_words(score), date, users

    def score_to_words(self,score):
        return {0:'Empty',1:'Nearly Empty',2:'Many Spots Open',3:'Spots Open',4:'Nearly Full',5:'Full'}[score]
    def __repr__(self):
        return '<Lot({0})>'.format(self.id)

class Checkin(db.Model):

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True)
    lot_id = Column(Integer, ForeignKey('lot.id'), nullable=False, index=True)
    score = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False, index=True)

    user = db.relationship('User', backref=db.backref('checkins', order_by='Checkin.date'))
    lot = db.relationship('Lot', backref=db.backref('checkins', order_by='Checkin.date'))

    def __repr__(self):
        return '<Checkin({0},{1},{2})>'.format(self.user, self.lot, self.score)
