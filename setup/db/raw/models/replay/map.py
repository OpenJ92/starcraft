from setup.db.raw.config import db 

class MAP(db.Model):
    __tablename__ = "MAP"

    __id__ = db.Column(db.Integer, primary_key = True)

    filename = db.Column(db.Text)
    filehash = db.Column(db.Text)
    name = db.Column(db.Text)
    author = db.Column(db.Text)
    description = db.Column(db.Text)
    website = db.Column(db.Text)
    minimap = db.Column(db.LargeBinary)

    replays = db.relationship('INFO', back_populates='map')

    @classmethod
    def process(cls, replay):
        conditions = cls.process_conditions(replay)
        if conditions:
            data = cls.process_raw_data(replay.map)
            depend_data = {}
            Map = MAP(**data, **depend_data)

            db.session.add(Map)
            db.session.commit()

    @classmethod
    def process_conditions(cls, replay):
        with open('setup/db/raw/utils/map_CHECK_filehash.sql') as f:
            query = f"{f.read()}".format(filehash=replay.map.filehash)
            condition = db.engine.execute(query).fetchall() == []
        return condition

    @classmethod
    def process_raw_data(cls, obj):
        return {
                        key
                        :
                        value 
                        for key,value 
                        in vars(obj).items()
                        if key in cls.columns
                }

    @classmethod
    def select_from_object(cls, obj):
        return db.session.query(cls).filter(cls.filehash==obj.filehash).first()

    columns = {
                "filename",
                "filehash",
                "name",
                "author",
                "description",
                "website",
                "minimap"
               }
