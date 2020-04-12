from setup.db.raw.models.datapack.unit_type import UNIT_TYPE
from setup.db.raw.config import db 

class ABILITY(db.Model):
    __tablename__ = "ABILITY"

    release_string = db.Column(db.Text)

    id = db.Column(db.Integer, primary_key = True)
    version = db.Column(db.Text)
    name = db.Column(db.Text)
    title = db.Column(db.Text)
    is_build = db.Column(db.Boolean)
    build_time = db.Column(db.Integer)
    build_unit = db.Column(db.Integer, db.ForeignKey('UNIT_TYPE.__id__'))

    @classmethod
    def process(cls, replay):
        release_string = replay.release_string
        conditions = True
        if conditions:
            objs = []
            for name, obj in replay.datapack.abilities.items():
                parents = cls.get_dependancies(obj, replay)
                data = {
                            key : value 
                            for key,value 
                            in vars(obj).items() 
                            if key!="build_unit"
                       }
                objs.append(ABILITY(**parents, **data))
            db.session.add_all(objs)
            db.session.commit()

    @classmethod
    def get_dependancies(cls, obj, replay):
        return { 'build_unit' : UNIT_TYPE.select_from_object(obj, replay) }
        

