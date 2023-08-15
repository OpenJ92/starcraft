from sqlalchemy import and_

from src.db.raw.config import db
from src.db.raw.models.datapack.unit_type import UNIT_TYPE


class ABILITY(db.Model):
    __tablename__ = "ABILITY"
    __table_args__ = {"schema": "datapack"}

    __id__ = db.Column(db.Integer, primary_key = True)

    release_string = db.Column(db.Text)

    id = db.Column(db.Integer)
    version = db.Column(db.Text)
    name = db.Column(db.Text)
    title = db.Column(db.Text)
    is_build = db.Column(db.Boolean)
    build_time = db.Column(db.Integer)

    __UNIT_TYPE__ = db.Column(db.Integer, db.ForeignKey('datapack.UNIT_TYPE.__id__'))
    build_unit = db.relationship('UNIT_TYPE', back_populates='abilities')


    basic_command_events = db.relationship('BasicCommandEvent',back_populates='ability')
    target_point_command_events = db.relationship('TargetPointCommandEvent',back_populates='ability')
    target_unit_command_events = db.relationship('TargetUnitCommandEvent',back_populates='ability')

    @classmethod
    def process(cls, replay):
        release_string = replay.release_string
        conditions = cls.process_conditions(replay)
        if conditions:
            objs = []
            for name, obj in replay.datapack.abilities.items():
                parents = cls.process_dependancies(obj, replay)
                data = {
                            key : value
                            for key,value
                            in vars(obj).items()
                            if key!="build_unit"
                       }
                objs.append(ABILITY(release_string=release_string,**parents,**data))
            db.session.add_all(objs)
            db.session.commit()


    @classmethod
    def process_conditions(cls, replay):
        with open('src/db/raw/utils/ability_CHECK_release_string.sql') as f:
            query = f"{f.read()}".format(release_string=replay.release_string)
            condition = db.engine.execute(query).fetchall() == []
        return condition

    @classmethod
    def process_dependancies(cls, obj, replay):
        N = obj.build_unit
        UT = None if not N else UNIT_TYPE.select_from_object(N, replay)
        return {
                    'build_unit'    : UT,
                    '__UNIT_TYPE__' : None if UT is None else UT.__id__
                }

    @classmethod
    def select_from_object(cls, obj, replay):
        return db.session.query(cls).\
                filter(
                        and_(
                              cls.id == obj.id,
                              cls.release_string == replay.release_string
                            )
                      ).first()
