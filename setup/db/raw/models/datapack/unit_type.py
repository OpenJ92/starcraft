from setup.db.raw.config import db 

class UNIT_TYPE(db.Model):
    __tablename__ = "UNIT_TYPE"

    id = db.Column(db.Integer, primary_key = True)
    version = db.Column(db.Text)
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
    def process(replay):
        release_string = replay.release_string
        if db.engine.execute(f"select release_string from starcraft.UNIT_TYPE where release_string = {release_string}"):
            pass
