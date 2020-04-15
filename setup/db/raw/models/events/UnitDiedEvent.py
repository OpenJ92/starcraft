from setup.db.raw.config import db 

from setup.db.raw.models.replay.info import INFO
from setup.db.raw.models.replay.player import PLAYER
from setup.db.raw.models.replay.objects import OBJECT

class UnitDiedEvent(db.Model):
    __tablename__ = "UnitDiedEvent"
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key = True)

    frame = db.Column(db.Integer)
    second = db.Column(db.Integer) 
    name = db.Column(db.Text)
    unit_id_index = db.Column(db.Integer)
    unit_id_recycle = db.Column(db.Integer)
    unit_id = db.Column(db.Integer)
    killer_pid = db.Column(db.Integer)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)

    #: The unit object that died
    ## unit
    __UNIT__ = db.Column(db.Integer, db.ForeignKey('replay.OBJECT.__id__'))
    unit = db.relationship(
                            'OBJECT',
                            primaryjoin='UnitDiedEvent.__UNIT__==OBJECT.__id__',
                            back_populates = 'death_event'
                          )

    #: A reference to the :class:`Unit` that killed this :class:`Unit`
    ## killing_unit
    __KILLING_UNIT__ = db.Column(db.Integer, db.ForeignKey('replay.OBJECT.__id__'))
    killing_unit = db.relationship(
                             'OBJECT',
                             primaryjoin='UnitDiedEvent.__KILLING_UNIT__==OBJECT.__id__',
                             back_populates = 'kill_event'
                                  )

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    info = db.relationship('INFO', back_populates = 'unit_died_events')

    __PLAYER__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    killing_player = db.relationship('PLAYER', back_populates = 'unit_died_events')

    @classmethod
    def process(cls, obj, replay):
        data = cls.process_object(obj)
        depend_data = cls.process_dependancies(obj, replay)
        basic_command_event = cls(**data, **depend_data)
        print(obj)
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
        killing_unit = None if not obj.killing_unit else OBJECT.select_from_object(obj.killing_unit, replay)
        killing_player = None if not obj.killing_player else PLAYER.select_from_object(obj.killing_player, replay)

        return {
                    'info' : info,
                    'unit' : unit,
                    'killing_unit' : killing_unit,
                    'killing_player' : killing_player
               }

    columns = {
                    "frame",
                    "second",
                    "name",
                    "unit_id_index",
                    "unit_id_recycle",
                    "unit_id",
                    "killer_pid",
                    "x",
                    "y"
              }

