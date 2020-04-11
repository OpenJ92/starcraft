from setup.db.raw.config import db 

class PLAYER(db.Model):
    __tablename__ = "PLAYER"
    id = db.Column(db.Integer, primary_key = True)
    sid = db.Column(db.Integer)
    team_id = db.Column(db.Integer)
    is_human = db.Column(db.Boolean)
    is_observer = db.Column(db.Boolean)
    is_referee = db.Column(db.Boolean)
    region = db.Column(db.Text)
    subregion = db.Column(db.Integer)
    toon_id = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    ## -- -- init_data good for scaled_rating
    ## -- init_data               <class 'dict'>
    clan_tag = db.Column(db.Text)
    name = db.Column(db.Text)
    combined_race_levels = db.Column(db.Integer)
    highest_league = db.Column(db.Integer)
    pid = db.Column(db.Integer)
    ## -- -- detail_data dictionary may be useful for player ID info
    ## -- detail_data             <class 'dict'>
    result = db.Column(db.Text)
    pick_race = db.Column(db.Text)
    play_race = db.Column(db.Text)
    replay_id = db.Column(db.Integer)
    ## PRIMARY KEY (__id__),
    ## FOREIGN KEY (replay_id) REFERENCES replay.info(__id__)
