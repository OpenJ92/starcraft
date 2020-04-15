from src.db.raw.config import db 

from src.db.raw.models.replay.player import PLAYER
from src.db.raw.models.replay.info import INFO

class PlayerSetupEvent(db.Model):
    __tablename__ = "PlayerSetupEvent"
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key = True)

    pid = db.Column(db.Integer)
    frame = db.Column(db.Integer)
    second = db.Column(db.Integer) 
    name = db.Column(db.Text)
    type = db.Column(db.Integer)
    uid = db.Column(db.Integer) 
    sid = db.Column(db.Integer)

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    info = db.relationship('INFO', back_populates = 'player_setup_events')

    @classmethod
    def process(cls, obj, replay):
        data = cls.process_object(obj)
        depend_data = cls.process_dependancies(obj, replay)
        control_group_event = cls(**data, **depend_data)
        print(obj)
        db.session.add(control_group_event)
        db.session.commit()


    @classmethod
    def process_object(cls, obj):
        return {
                        key
                        :
                        value 
                        for key,value 
                        in vars(obj).items()
                        if key in cls.columns
                }

    @classmethod
    def process_dependancies(cls, obj, replay):
        info = None if not replay else INFO.select_from_object(replay)
        return {
                    'info' : info,
               }

    columns = {
                    "pid",
                    "frame",
                    "second",
                    "name",
                    "type",
                    "uid",
                    "sid"
            }

