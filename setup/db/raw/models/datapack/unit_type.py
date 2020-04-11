from setup.db.raw.config import db 

class UNIT_TYPE(db.Model):
    __tablename__ = "UNIT_TYPE"

    __id__ = db.Column(db.Integer, primary_key = True)
    id = db.Column(db.Integer)
    release_string = db.Column(db.Text)
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
            string_ = f"{f.read()}".format(release_string = replay.release_string)
            test = db.engine.execute(string_).rowcount == 0
        return test

