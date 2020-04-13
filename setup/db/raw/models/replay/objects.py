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

    ## There's a chance that this information could be back_populated through
    ## a relationship to the UNIT_DIED_EVENT in the events schema.
    ## 
    ## https://docs.sqlalchemy.org/en/13/orm/self_referential.html
    ##      __KU_id__ = db.Column(db.Integer, db.ForeignKey('replay.OBJECT.__id__'))
    ##      killing_unit = db.relationship('OBJECT', remote_side='OBJECT.__KU_id__')

    @classmethod
    def process(cls, replay):
        objs = []
        depend_data = cls.process_dependancies(replay)
        conditions = cls.process_conditions(replay)
        if conditions: 
            for _, obj in replay.objects.items():
                print(obj, type(obj))
                data = cls.process_object(obj)
                derived_data = cls.process_derived(obj, replay)
                objs.append(
                                cls(
                                        **data,
                                        **derived_data,
                                        **depend_data
                                   )
                            )
            db.session.add_all(objs)
            db.session.commit()

    @classmethod
    def process_conditions(cls, replay):
        with open('setup/db/raw/utils/info_CHECK_filehash.sql') as f:
            query = f"{f.read()}".format(filehash=replay.filehash)
            condition = db.engine.execute(query).fetchall() == []
        return condition

    @classmethod
    def process_dependancies(cls, replay):
        UT = None if not replay else INFO.select_from_object(replay)
        return { 'replay' : UT, '__INFO__' : UT.__id__ }

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
    def process_derived(cls, obj, replay):

        try:
            unit_type = UNIT_TYPE.select_from_object(obj._type_class, replay),
            killing_player = PLAYER.select_from_object(obj.killing_player, replay)
            killed_by = PLAYER.select_from_object(obj.killed_by, replay)
            owner = PLAYER.select_from_object(obj.owner, replay)

            ## __UNIT_TYPE__ = unit_type[0].__id__ if not unit_type else None
            ## __KILLED__= killing_player[0].__id__ if killing_player else None
            ## __KILLEDBY__ = killed_by[0].__id__ if killed_by else None
            ## __OWNER__ = owner[0].__id__ if owner else None

            return {
                        'name' : obj.name,
                        'location_x' : obj.location[0],
                        'location_y' : obj.location[1],
                        'owner' : owner,
                        'killing_player' : killing_player,
                        'killed_by' : killed_by,
                        'unit_type' : unit_type[0] ## why is this returning a tuple?
                        ## '__OWNER__' : __OWNER__,
                        ## '__KILLED__' : __KILLED__,
                        ## '__KILLEDBY__' : __KILLEDBY__,
                        ##'__UNIT_TYPE__' : __UNIT_TYPE__ 
                   }
        except Exception as e:
            ## look to perhaps use logging here.
            print(e)
            return {}

    @classmethod
    def select_from_object(cls):
        pass

    columns = {
                    "id",
                    "started_at",
                    "finished_at",
                    "died_at"
              }
