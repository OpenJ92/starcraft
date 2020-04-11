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
        test = db.engine.execute(f"select release_string from \"public\".\"UNIT_TYPE\" where release_string = \'{release_string}\'")
        if not test.rowcount:
            import pdb;pdb.set_trace()
            objs = []
            for name, obj in replay.datapack.units.items():
                objs.append(UNIT_TYPE(release_string = release_string, **vars(obj)))
            db.session.add_all(objs)
            db.session.commit()

    @classmethod
    def process_conditions(cls, replay):
        pass

