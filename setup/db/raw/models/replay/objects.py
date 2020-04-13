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
    name = db.Column(db.Text)

    location_x = db.Column(db.Integer)
    location_y = db.Column(db.Integer)

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    replay = db.relationship('INFO', back_populates='objects')

    __OWNER__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    owner = db.relationship(
                                'PLAYER', 
                                primaryjoin='OBJECT.__OWNER__==PLAYER.__id__', 
                                back_populates='owned_objects'
                            )

    __KILLED__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    killing_player = db.relationship(
                                'PLAYER', 
                                primaryjoin='OBJECT.__KILLED__==PLAYER.__id__', 
                                back_populates='killing_player_objs'
                                    )

    __KILLEDBY__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    killed_by = db.relationship(
                                'PLAYER', 
                                primaryjoin='OBJECT.__KILLEDBY__==PLAYER.__id__', 
                                back_populates='killed_by_objs'
                               )

    __UNIT_TYPE__ = db.Column(db.Integer, db.ForeignKey('datapack.UNIT_TYPE.__id__'))
    unit_type = db.relationship('UNIT_TYPE', back_populates='objects')

    ## https://docs.sqlalchemy.org/en/13/orm/self_referential.html
    __KU_id__ = db.Column(db.Integer, db.ForeignKey('replay.OBJECT.__id__'))
    killing_unit = db.relationship('OBJECT', remote_side='OBJECT.__KU_id__')

    @classmethod
    def process(cls, replay):
        objs = []
        players, replay = cls.process_dependancies(replay)
        conditions = cls.process_condtions()
        if condtions: 
            for _, obj in relpay.objects.items():
                data = cls.process_object(obj)
                derived_data = cls.process_derived(obj, players, replay)
                objs.append(
                                cls(
                                        **data,
                                        **derived_data,
                                        **replay 
                                   )
                            )


    @classmethod
    def process_conditions(cls):
        return True

    @classmethod
    def process_dependancies(cls, replay):
        UT = None if not replay else INFO.select_from_object(replay)
        PLAYERS = {
                    player
                    :
                    None if not player else PLAYER.select_from_object(player)
                    for player
                    in replay.players
                  }
        return PLAYERS, { 'replay' : UT, '__INFO__' : UT.__id__ }

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
    def process_derived(cls, obj, players, replay):
        return {
                    'name' : obj.name,
                    'location_x' : obj.location[0],
                    'location_y' : obj.location[1],
                    'owner' : players[obj.owner], 
                    '__OWNER__' : players[obj.owner].__id__,
                    'killing_player' : players[obj.killing_player], 
                    '__KILLED__' : players[obj.killing_player].__id__, 
                    'killed_by' : players[obj.killed_by], 
                    '__KILLEDBY__' : players[obj.killed_by].__id__,
                    'unit_type' : UNIT_TYPE.select_from_object(obj.unit_type, replay),
                    '__UNIT_TYPE__' : UNIT_TYPE.select_from_object(obj.unit_type, replay).__id__
               }

    @classmethod
    def select_from_object(cls):
        pass

    columns = {
                    "id",
                    "started_at",
                    "finished_at",
                    "died_at"
              }
