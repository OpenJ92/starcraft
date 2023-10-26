from src.db.raw.config import db

from src.db.raw.models.replay.player import PLAYER
from src.db.raw.models.replay.info import INFO


class PlayerLeaveEvent(db.Model):
    __tablename__ = "PlayerLeaveEvent"
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key=True)

    pid = db.Column(db.Integer)
    frame = db.Column(db.Integer)
    second = db.Column(db.Integer)
    name = db.Column(db.Text)
    is_local = db.Column(db.Boolean)

    leave_reason = db.Column(db.Integer)

    __PLAYER__ = db.Column(db.Integer, db.ForeignKey("replay.PLAYER.__id__"))
    player = db.relationship("PLAYER", back_populates="player_leave_events")

    __INFO__ = db.Column(db.Integer, db.ForeignKey("replay.INFO.__id__"))
    info = db.relationship("INFO", back_populates="player_leave_events")

    @classmethod
    def process(cls, obj, replay):
        data = cls.process_object(obj)
        depend_data = cls.process_dependancies(obj, replay)
        derived_data = cls.process_derived(obj)
        control_group_event = cls(**data, **depend_data, **derived_data)
        db.session.add(control_group_event)
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

        return {
            "info": info,
            "player": player,
        }

    @classmethod
    def process_derived(cls, obj):
        return {"leave_reason": obj.data["leave_reason"]}

    columns = {"pid", "frame", "second", "name", "is_local"}
