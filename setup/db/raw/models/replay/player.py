from collections import namedtuple
from sqlalchemy import and_

from setup.db.raw.config import db 
from setup.db.raw.models.replay.info import INFO

class PLAYER(db.Model):
    __tablename__ = "PLAYER"
    __table_args__ = {"schema": "replay"}

    __id__ = db.Column(db.Integer, primary_key = True)

    sid = db.Column(db.Integer)
    team_id = db.Column(db.Integer)
    is_human = db.Column(db.Boolean)
    is_observer = db.Column(db.Boolean)
    is_referee = db.Column(db.Boolean)
    region = db.Column(db.Text)
    subregion = db.Column(db.Integer)
    toon_id = db.Column(db.BigInteger)
    uid = db.Column(db.Integer)
    clan_tag = db.Column(db.Text)
    name = db.Column(db.Text)
    combined_race_levels = db.Column(db.BigInteger)
    highest_league = db.Column(db.Integer)
    pid = db.Column(db.Integer)
    result = db.Column(db.Text)
    pick_race = db.Column(db.Text)
    play_race = db.Column(db.Text)
    
    id = db.Column(db.Integer)

    owned_objects = db.relationship(
                        'OBJECT', 
                        primaryjoin='OBJECT.__OWNER__==PLAYER.__id__', 
                        back_populates='owner'
                                   )
    killing_player_objs = db.relationship(
                        'OBJECT', 
                        primaryjoin='OBJECT.__KILLED__==PLAYER.__id__', 
                        back_populates='killing_player'
                                         )

    killed_by_objs = db.relationship(
                        'OBJECT', 
                        primaryjoin='OBJECT.__KILLEDBY__==PLAYER.__id__', 
                        back_populates='killed_by'
                                    )


    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    replay = db.relationship('INFO', back_populates='players')

    basic_command_events=db.relationship('BasicCommandEvent',back_populates='player')
    chat_events=db.relationship('ChatEvent', back_populates='player')
    camera_events = db.relationship('CameraEvent',back_populates='player')
    control_group_events = db.relationship('ControlGroupEvent',back_populates='player')
    get_control_group_events = db.relationship('GetControlGroupEvent',back_populates='player')
    set_control_group_events = db.relationship('SetControlGroupEvent',back_populates='player')

    @classmethod
    def process(cls, replay):
        objs = []
        parents = cls.process_dependancies(replay)
        condition = cls.process_conditions(replay)
        if condition:
            for obj in replay.players:
                print(obj)
                data = cls.process_object(obj)
                data_derived = cls.process_derived(obj)
                objs.append(cls(**data, **parents, **data_derived))
            db.session.add_all(objs)
            db.session.commit()

    @classmethod
    def process_conditions(cls, replay):
        ## What is the condition that must hold for su to proceed to object
        ## creation and db injection?
        return True

    @classmethod
    def process_dependancies(cls, replay):
        UT = None if not replay else INFO.select_from_object(replay)
        return {
                    'replay' : UT,
                    '__INFO__' : None if UT else UT.__id__
               }

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
    def process_derived(cls, obj):
        return {
                        'id' : obj.detail_data['bnet']['uid']
               }

    @classmethod
    def select_from_object(cls, obj, replay):
        NULLPLAYER = namedtuple('NULLPLAYER', ('detail_data',))
        obj = obj if obj else NULLPLAYER({'bnet':{'uid':-1}})
        return db.session.query(cls).filter(
                                    and_(
                                          cls.id==obj.detail_data['bnet']['uid'],
                                          cls.__INFO__==INFO.select_from_object(replay).__id__
                                         )
                                    ).one_or_none()
                                          
        pass

    columns = {
                    "sid",
                    "team_id",
                    "is_human",
                    "is_observer",
                    "is_referee",
                    "region",
                    "subregion",
                    "toon_id",
                    "uid",
                    "clan_tag",
                    "name",
                    "combined_race_levels",
                    "highest_league",
                    "pid",
                    "result",
                    "pick_race",
                    "play_race"
            }
