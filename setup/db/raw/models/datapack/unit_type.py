from sqlalchemy import and_

from setup.db.raw.config import db 

class UNIT_TYPE(db.Model):
    __tablename__ = "UNIT_TYPE"

    __id__ = db.Column(db.Integer, primary_key = True)

    release_string = db.Column(db.Text)

    id = db.Column(db.Integer)
    str_id = db.Column(db.Text)
    name = db.Column(db.Text)
    title = db.Column(db.Text)
    race = db.Column(db.Text)
    minerals = db.Column(db.Integer)
    vespene = db.Column(db.Integer)
    supply = db.Column(db.Integer)
    is_building = db.Column(db.Boolean)
    is_army = db.Column(db.Boolean)
    is_worker = db.Column(db.Boolean)

    @classmethod
    def process(cls, replay):
        release_string = replay.release_string
        conditions = cls.process_conditions(replay)
        if conditions:
            objs = []
            for name, obj in replay.datapack.units.items():
                objs.append(UNIT_TYPE(release_string = release_string, **vars(obj)))
            db.session.add_all(objs)
            db.session.commit()

    @classmethod
    def process_conditions(cls, replay):
        with open('setup/db/raw/utils/unit_type_CHECK_release_string.sql') as f:
            query = f"{f.read()}".format(release_string=replay.release_string)
            condition = db.engine.execute(query).returns_rows
        return condition

    @classmethod
    def get_dependancies(cls):
        pass

    @classmethod
    def select_from_object(cls, obj, replay):
        ## note that this returns more than one row... There are duplicates in 
        ## the above process function.
        return db.session.query(UNIT_TYPE).\
                filter(
                        and_(
                              UNIT_TYPE.id == obj.id,
                              UNIT_TYPE.release_string == replay.release_string
                            )
                      ).first()
