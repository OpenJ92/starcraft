from setup.db.raw.config import db 

from setup.db.raw.models.replay.info import INFO
from setup.db.raw.models.replay.player import PLAYER
from setup.db.raw.models.datapack.unit_type import UNIT_TYPE

class OBJECT(db.Model):
    __tablename__ = "OBJECT"
    __table_args__ = {"schema": "replay"}

    __id__ = db.Column(db.Integer, primary_key = True)

    id = db.Column(db.Integer)
    started_at = db.Column(db.Integer)
    finished_at = db.Column(db.Integer)
    died_at = db.Column(db.Integer)

    location_x = db.Column(db.Integer)
    location_y = db.Column(db.Integer)

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    replay = db.relationship('INFO', back_populates='objects')

    __OWNER__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    owner = db.relationship(
                                'PLAYER', 
                                primaryjoin=__OWNER__==PLAYER.__id__, 
                                back_populates='owned_objects'
                            )

    __KILLED__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    killing_player = db.relationship(
                                'PLAYER', 
                                primaryjoin=__KILLED__==PLAYER.__id__, 
                                back_populates='killing_player_objs'
                                    )

    __KILLEDBY__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    killed_by = db.relationship(
                                'PLAYER', 
                                primaryjoin=__KILLEDBY__==PLAYER.__id__, 
                                back_populates='killed_by_objs'
                               )

    __UNIT_TYPE__ = db.Column(db.Integer, db.ForeignKey('datapack.UNIT_TYPE.__id__'))
    unit_type = db.relationship('UNIT_TYPE', back_populates='objects')

    @classmethod
    def process(cls):
        pass

    @classmethod
    def process_conditions(cls):
        pass

    @classmethod
    def process_dependancies(cls):
        pass

    @classmethod
    def process_object(cls):
        pass

    @classmethod
    def process_derived(cls):
        pass

    @classmethod
    def select_from_object(cls):
        pass
