## Note! We do not hook unit upkeeper onto OBJECTS, just the 
## controller. However, the pid of the upkeeper is maintained

from src.db.raw.config import db 

from src.db.raw.models.replay.player import PLAYER
from src.db.raw.models.replay.info import INFO
from src.db.raw.models.replay.objects import OBJECT

class UnitBornEvent(db.Model):
    __tablename__ = "UnitBornEvent"
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key = True)

    frame = db.Column(db.Integer)
    second = db.Column(db.Integer) 
    name = db.Column(db.Text)
    unit_id_index = db.Column(db.Integer)
    unit_id_recycle = db.Column(db.Integer)
    unit_id = db.Column(db.Integer)
    unit_type_name = db.Column(db.Text)
    control_pid = db.Column(db.Integer)
    upkeep_pid = db.Column(db.Integer)
    x = db.Column(db.Float)
    y = db.Column(db.Float)

    __PLAYER__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    unit_controller = db.relationship('PLAYER', back_populates = 'unit_born_events')

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    info = db.relationship('INFO', back_populates = 'unit_born_events')

    __OBJECT__ = db.Column(db.Integer, db.ForeignKey('replay.OBJECT.__id__'))
    unit = db.relationship('OBJECT', back_populates = 'unit_born_events')

    @classmethod
    def process(cls, obj, replay):
        data = cls.process_object(obj)
        depend_data = cls.process_dependancies(obj, replay)
        basic_command_event = cls(**data, **depend_data)
        db.session.add(basic_command_event)
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
        unit_controller = None if not obj.unit_controller else PLAYER.select_from_object(obj.unit_controller, replay)
        unit = None if not obj.unit else OBJECT.select_from_object(obj.unit, replay)

        return {
                    'info' : info,
                    'unit_controller' : unit_controller,
                    'unit' : unit
               }

    columns = {
                    "frame",
                    "second",
                    "name",
                    "unit_id_index",
                    "unit_id_recycle",
                    "unit_id",
                    "unit_type_name",
                    "control_pid",
                    "upkeep_pid",
                    "x",
                    "y"
               }
