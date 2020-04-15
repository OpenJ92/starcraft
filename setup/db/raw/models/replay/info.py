from setup.db.raw.config import db 

from setup.db.raw.models.replay.map import MAP

class INFO(db.Model):
    __tablename__ = "INFO"
    __table_args__ = {"schema": "replay"}

    __id__ = db.Column(db.Integer, primary_key = True)

    filename = db.Column(db.Text)
    filehash = db.Column(db.Text)
    load_level = db.Column(db.Integer)
    speed = db.Column(db.Text)
    type = db.Column(db.Text)
    game_type = db.Column(db.Text)
    real_type = db.Column(db.Text)
    category = db.Column(db.Text)
    is_ladder = db.Column(db.Boolean)
    is_private = db.Column(db.Boolean)
    map_hash = db.Column(db.Text)
    region = db.Column(db.Text)
    game_fps = db.Column(db.Float)
    frames = db.Column(db.Integer)
    build = db.Column(db.Integer)
    base_build = db.Column(db.Integer)
    release_string = db.Column(db.Text)
    amm = db.Column(db.Integer)
    competitive = db.Column(db.Integer)
    practice = db.Column(db.Integer)
    cooperative = db.Column(db.Integer)
    battle_net = db.Column(db.Integer)
    hero_duplicates_allowed = db.Column(db.Integer)
    map_name = db.Column(db.Text)
    expansion = db.Column(db.Text)
    windows_timestamp = db.Column(db.BigInteger)
    unix_timestamp = db.Column(db.BigInteger)
    end_time = db.Column(db.DateTime)
    time_zone = db.Column(db.Float)
    start_time = db.Column(db.DateTime)
    date = db.Column(db.DateTime)

    players = db.relationship('PLAYER', back_populates='replay')
    objects = db.relationship('OBJECT', back_populates='replay')

    basic_command_events = db.relationship('BasicCommandEvent',back_populates='info')
    chat_events = db.relationship('ChatEvent',back_populates='info')
    camera_events = db.relationship('CameraEvent',back_populates='info')
    control_group_events = db.relationship('ControlGroupEvent',back_populates='info')
    get_control_group_events = db.relationship('GetControlGroupEvent',back_populates='info')
    set_control_group_events = db.relationship('SetControlGroupEvent',back_populates='info')
    player_stats_events = db.relationship('PlayerStatsEvent',back_populates='info')
    player_leave_events = db.relationship('PlayerLeaveEvent',back_populates='info')
    player_setup_events = db.relationship('PlayerSetupEvent',back_populates='info')
    target_point_command_events = db.relationship('TargetPointCommandEvent',back_populates='info')
    target_unit_command_events = db.relationship('TargetUnitCommandEvent',back_populates='info')
    upgrade_complete_events = db.relationship('UpgradeCompleteEvent',back_populates='info')
    unit_born_events = db.relationship('UnitBornEvent',back_populates='info')
    unit_done_events = db.relationship('UnitDoneEvent',back_populates='info')
    unit_init_events = db.relationship('UnitInitEvent',back_populates='info')
    unit_type_change_events = db.relationship('UnitTypeChangeEvent',back_populates='info')

    __MAP__ = db.Column(db.Integer, db.ForeignKey('replay.MAP.__id__'))
    map = db.relationship('MAP', back_populates='replays')

    @classmethod
    def process(cls, replay):
        conditions = cls.process_conditions(replay)
        if conditions:
            data = cls.process_object(replay)
            depend_data = cls.process_dependancies(replay) 
            info = INFO(**data, **depend_data)
            print(replay)

            db.session.add(info)
            db.session.commit()

    @classmethod
    def process_conditions(cls, replay):
        with open('setup/db/raw/utils/info_CHECK_filehash.sql') as f:
            query = f"{f.read()}".format(filehash=replay.filehash)
            condition = db.engine.execute(query).fetchall() == []
        return condition

    @classmethod
    def process_object(cls, replay):
        return {
                        key
                        :
                        value 
                        for key,value 
                        in vars(replay).items()
                        if key in cls.columns
                }

    @classmethod
    def process_dependancies(cls, replay):
        N = replay.map
        UT = None if not N else MAP.select_from_object(N)
        return { 
                    'map'    : UT,
                    '__MAP__' : None if UT is None else UT.__id__ 
               }

    @classmethod
    def select_from_object(cls, obj):
        return db.session.query(cls).filter(cls.filehash==obj.filehash).first()

    columns = [
                    "id",
                    "filename",
                    "filehash",
                    "load_level",
                    "speed",
                    "type",
                    "game_type",
                    "real_type",
                    "category",
                    "is_ladder",
                    "is_private",
                    "map_hash",
                    "region",
                    "game_fps",
                    "frames",
                    "build",
                    "base_build",
                    "release_string",
                    "amm",
                    "competitive",
                    "practice",
                    "cooperative",
                    "battle_net",
                    "hero_duplicates_allowed",
                    "map_name",
                    "expansion",
                    "windows_timestamp",
                    "unix_timestamp",
                    "end_time",
                    "time_zone",
                    "start_time",
                    "date"
              ]

