from setup.db.raw.config import db 

from setup.db.raw.models.replay.player import PLAYER
from setup.db.raw.models.replay.info import INFO

class ChatEvent(db.Model):
    __tablename__ = "ChatEvent"
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key = True)

    pid = db.Column(db.Integer)
    frame = db.Column(db.Integer)
    second = db.Column(db.Integer) 
    name = db.Column(db.Text)
    target = db.Column(db.Integer)  
    text = db.Column(db.Text)
    to_all = db.Column(db.Boolean)
    to_allies = db.Column(db.Boolean)
    to_observers = db.Column(db.Boolean)

    __PLAYER__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    player = db.relationship('PLAYER', back_populates = 'chat_events')

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    info = db.relationship('INFO', back_populates = 'chat_events')
