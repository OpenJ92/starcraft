from setup.db.raw.config import db 

from setup.db.raw.models.datapack.ability import ABILITY
from setup.db.raw.models.replay.info import INFO
from setup.db.raw.models.replay.player import PLAYER

class BasicCommandEvent(db.Model):
    __tablename__ = " BasicCommandEvent" 
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key = True)

    pid = db.Column(db.Integer)
    frame = db.Column(db.Integer)
    second = db.Column(db.Integer)
    is_local = db.Column(db.Boolean)
    name = db.Column(db.Text)
    has_ability = db.Column(db.Boolean)
    ability_link = db.Column(db.Integer)
    command_index = db.Column(db.Integer)
    ability_name = db.Column(db.Text)
    
    __PLAYER__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    player = db.relationship('PLAYER', back_populates = 'events')

    __ABILITY__ =  db.Column(db.Integer, db.ForeignKey('datapack.ABILITY.__id__'))
    ability = db.relationship('ABILITY', back_populates = 'events')
