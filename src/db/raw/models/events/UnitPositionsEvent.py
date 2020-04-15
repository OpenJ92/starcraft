from uuid import uuid4

from src.db.raw.config import db 

from src.db.raw.models.replay.info import INFO
from src.db.raw.models.replay.objects import OBJECT

class UnitPositionsEvent(db.Model):
    __tablename__ = "UnitPositionsEvent"
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key = True)

    frame = db.Column(db.Integer)
    second = db.Column(db.Integer) 
    name = db.Column(db.Text)

    position_id = db.Column(db.Text)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    info = db.relationship('INFO', back_populates = 'unit_positions_events')

    __OBJECT__ = db.Column(db.Integer, db.ForeignKey('replay.OBJECT.__id__'))
    unit = db.relationship('OBJECT', back_populates = 'unit_positions_events')

    @classmethod
    def process(cls, obj, replay):
        objs = []
        data = cls.process_object(obj)
        position_id = str(uuid4())
        for unit, (x, y) in obj.units.items():
            depend_data = cls.process_dependancies(unit, replay)
            objs.append(cls(**data, **depend_data, x=x, y=y,position_id=position_id))
            print(unit)
        print(obj)
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
    def process_dependancies(cls, _unit, replay):
        info = None if not replay else INFO.select_from_object(replay)
        unit = None if not _unit else OBJECT.select_from_object(_unit, replay)

        return {
                    'info' : info,
                    'unit' : unit
               }

    columns = {
                    "frame",
                    "second",
                    "name"
              }
