from setup.db.raw.config import db 

class ABILITY(db.Model):
    __tablename__ = "ABILITY"

    id = db.Column(db.Integer, primary_key = True)
    version = db.Column(db.Text)
    name = db.Column(db.Text)
    title = db.Column(db.Text)
    is_build = db.Column(db.Boolean)
    build_time = db.Column(db.Integer)
    build_unit = db.Column(db.Integer, db.ForeignKey('UNIT_TYPE.__id__'))

