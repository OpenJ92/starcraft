from uuid import uuid4

from src.db.raw.config import db 

from src.db.raw.models.replay.info import INFO
from src.db.raw.models.replay.player import PLAYER
from src.db.raw.models.replay.objects import OBJECT

class SelectionEvent(db.Model):
    __tablename__ = "SelectionEvent"
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key = True)

    pid = db.Column(db.Integer)
    frame = db.Column(db.Integer)
    second = db.Column(db.Integer) 
    name = db.Column(db.Text)
    is_local = db.Column(db.Boolean)
    control_group = db.Column(db.Integer)

    selection_id = db.Column(db.Text)

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    info = db.relationship('INFO', back_populates = 'selection_events')

    __PLAYER__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    player = db.relationship('PLAYER', back_populates = 'selection_events')

    __OBJECT__ = db.Column(db.Integer, db.ForeignKey('replay.OBJECT.__id__'))
    unit = db.relationship('OBJECT', back_populates = 'selection_events')

    @classmethod
    def process(cls, obj, replay):
        objs = []
        data = cls.process_object(obj)
        selection_id = str(uuid4())
        for unit in obj.new_units:
            depend_data = cls.process_dependancies(unit, obj, replay)
            objs.append(cls(**data, **depend_data, selection_id=selection_id))
        db.session.add_all(objs)
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
    def process_dependancies(cls, _unit, obj, replay):
        info = None if not replay else INFO.select_from_object(replay)
        player = Nont if not obj.player else PLAYER.select_from_object(obj.player, replay)
        unit = None if not _unit else OBJECT.select_from_object(_unit, replay)

        return {
                    'info' : info,
                    'player' : player,
                    'unit' : unit
               }

    columns = {
                    "pid",
                    "frame",
                    "second",
                    "name",
                    "is_local",
                    "control_group"
              }
