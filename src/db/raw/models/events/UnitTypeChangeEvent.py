from src.db.raw.config import db 

from src.db.raw.models.replay.info import INFO
from src.db.raw.models.replay.objects import OBJECT
from src.db.raw.models.datapack.unit_type import UNIT_TYPE

class UnitTypeChangeEvent(db.Model):
    __tablename__ = "UnitTypeChangeEvent"
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key = True)

    frame = db.Column(db.Integer)
    second = db.Column(db.Integer) 
    name = db.Column(db.Text)
    unit_id_index = db.Column(db.Integer)
    unit_id_recycle = db.Column(db.Integer)
    unit_id = db.Column(db.Integer)

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    info = db.relationship('INFO', back_populates = 'unit_type_change_events')

    __OBJECT__ = db.Column(db.Integer, db.ForeignKey('replay.OBJECT.__id__'))
    unit = db.relationship('OBJECT', back_populates = 'unit_type_change_events')

    __UNIT_TYPE__ = db.Column(db.Integer, db.ForeignKey('datapack.UNIT_TYPE.__id__'))
    unit_type = db.relationship('UNIT_TYPE')

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
        unit = None if not obj.unit else OBJECT.select_from_object(obj.unit, replay)
        unit_type = None if not obj.unit_type_name else UNIT_TYPE.select_from_str_id(obj.unit_type_name, replay)

        return {
                    'info' : info,
                    'unit' : unit,
                    'unit_type' : unit_type
               }

    columns = {
                    "frame",
                    "second",
                    "name",
                    "unit_id_index",
                    "unit_id_recycle",
                    "unit_id"
              }
