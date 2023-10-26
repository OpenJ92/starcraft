from src.db.raw.config import db

from src.db.raw.models.datapack.ability import ABILITY
from src.db.raw.models.replay.info import INFO
from src.db.raw.models.replay.player import PLAYER


class BasicCommandEvent(db.Model):
    __tablename__ = " BasicCommandEvent"
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key=True)

    pid = db.Column(db.Integer)
    frame = db.Column(db.Integer)
    second = db.Column(db.Integer)
    is_local = db.Column(db.Boolean)
    name = db.Column(db.Text)
    has_ability = db.Column(db.Boolean)
    ability_link = db.Column(db.Integer)
    command_index = db.Column(db.Integer)
    ability_name = db.Column(db.Text)

    __PLAYER__ = db.Column(db.Integer, db.ForeignKey("replay.PLAYER.__id__"))
    player = db.relationship("PLAYER", back_populates="basic_command_events")

    __INFO__ = db.Column(db.Integer, db.ForeignKey("replay.INFO.__id__"))
    info = db.relationship("INFO", back_populates="basic_command_events")

    __ABILITY__ = db.Column(db.Integer, db.ForeignKey("datapack.ABILITY.__id__"))
    ability = db.relationship("ABILITY", back_populates="basic_command_events")

    @classmethod
    def process(cls, obj, replay):
        data = cls.process_object(obj)
        depend_data = cls.process_dependancies(obj, replay)
        basic_command_event = cls(**data, **depend_data)
        db.session.add(basic_command_event)
        db.session.commit()

    @classmethod
    def process_object(cls, obj):
        return {key: value for key, value in vars(obj).items() if key in cls.columns}

    @classmethod
    def process_dependancies(cls, obj, replay):
        info = None if not replay else INFO.select_from_object(replay)
        player = (
            None if not obj.player else PLAYER.select_from_object(obj.player, replay)
        )
        ability = (
            None if not obj.ability else ABILITY.select_from_object(obj.ability, replay)
        )

        return {"info": info, "player": player, "ability": ability}

    columns = {
        "pid",
        "frame",
        "second",
        "is_local",
        "name",
        "has_ability",
        "ability_link",
        "command_index",
        "ability_name",
    }
