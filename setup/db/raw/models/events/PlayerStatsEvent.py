from setup.db.raw.config import db 

from setup.db.raw.models.replay.player import PLAYER
from setup.db.raw.models.replay.info import INFO

class PlayerStatsEvent(db.Model):
    __tablename__ = "PlayerStatsEvent"
    __table_args__ = {"schema": "events"}

    __id__ = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    minerals_current = db.Column(db.Float)
    vespene_current = db.Column(db.Float)
    minerals_collection_rate = db.Column(db.Float)
    vespene_collection_rate = db.Column(db.Float)
    workers_active_count = db.Column(db.Float)
    minerals_used_in_progress_army = db.Column(db.Float)
    minerals_used_in_progress_economy = db.Column(db.Float)
    minerals_used_in_progress_technology = db.Column(db.Float)
    minerals_used_in_progress = db.Column(db.Float)
    vespene_used_in_progress_army = db.Column(db.Float)
    vespene_used_in_progress_economy = db.Column(db.Float)
    vespene_used_in_progress_technology = db.Column(db.Float)
    vespene_used_in_progress = db.Column(db.Float)
    resources_used_in_progress = db.Column(db.Float)
    minerals_used_current_army = db.Column(db.Float)
    minerals_used_current_economy = db.Column(db.Float)
    minerals_used_current_technology = db.Column(db.Float)
    minerals_used_current = db.Column(db.Float)
    vespene_used_current_army = db.Column(db.Float)
    vespene_used_current_economy = db.Column(db.Float)
    vespene_used_current_technology = db.Column(db.Float)
    vespene_used_current = db.Column(db.Float)
    resources_used_current = db.Column(db.Float)
    minerals_lost_army = db.Column(db.Float)
    minerals_lost_economy = db.Column(db.Float)
    minerals_lost_technology = db.Column(db.Float)
    minerals_lost = db.Column(db.Float)
    vespene_lost_army = db.Column(db.Float)
    vespene_lost_economy = db.Column(db.Float)
    vespene_lost_technology = db.Column(db.Float)
    vespene_lost = db.Column(db.Float)
    resources_lost = db.Column(db.Float)
    minerals_killed_army = db.Column(db.Float)
    minerals_killed_economy = db.Column(db.Float)
    minerals_killed_technology = db.Column(db.Float)
    minerals_killed = db.Column(db.Float)
    vespene_killed_army = db.Column(db.Float)
    vespene_killed_economy = db.Column(db.Float)
    vespene_killed_technology = db.Column(db.Float)
    vespene_killed = db.Column(db.Float)
    resources_killed = db.Column(db.Float)
    food_used = db.Column(db.Float)
    food_made = db.Column(db.Float)
    minerals_used_active_forces = db.Column(db.Float)
    vespene_used_active_forces = db.Column(db.Float)
    ff_minerals_lost_army = db.Column(db.Float)
    ff_minerals_lost_economy = db.Column(db.Float)
    ff_minerals_lost_technology = db.Column(db.Float)
    ff_vespene_lost_army = db.Column(db.Float)
    ff_vespene_lost_economy = db.Column(db.Float)
    ff_vespene_lost_technology = db.Column(db.Float)

    __PLAYER__ = db.Column(db.Integer, db.ForeignKey('replay.PLAYER.__id__'))
    player = db.relationship('PLAYER', back_populates = 'player_stats_events')

    __INFO__ = db.Column(db.Integer, db.ForeignKey('replay.INFO.__id__'))
    info = db.relationship('INFO', back_populates = 'player_stats_events')

    @classmethod
    def process(cls, obj, replay):
        data = cls.process_object(obj)
        depend_data = cls.process_dependancies(obj, replay)
        control_group_event = cls(**data, **depend_data)
        print(obj)
        db.session.add(control_group_event)
        db.session.commit()


    @classmethod
    def process_object(cls, obj):
        return {
                        key
                        :
                        value 
                        for key,value 
                        in vars(obj).items()
                        if key in cls.columns
                }

    @classmethod
    def process_dependancies(cls, obj, replay):
        info = None if not replay else INFO.select_from_object(replay)
        player = None if not obj.player else PLAYER.select_from_object(obj.player, replay)

        return {
                    'info' : info,
                    'player' : player,
               }

    columns = {
                    "name",
                    "second",
                    "minerals_current",
                    "vespene_current",
                    "minerals_collection_rate",
                    "vespene_collection_rate",
                    "workers_active_count",
                    "minerals_used_in_progress_army",
                    "minerals_used_in_progress_economy",
                    "minerals_used_in_progress_technology",
                    "minerals_used_in_progress",
                    "vespene_used_in_progress_army",
                    "vespene_used_in_progress_economy",
                    "vespene_used_in_progress_technology",
                    "vespene_used_in_progress",
                    "resources_used_in_progress",
                    "minerals_used_current_army",
                    "minerals_used_current_economy",
                    "minerals_used_current_technology",
                    "minerals_used_current",
                    "vespene_used_current_army",
                    "vespene_used_current_economy",
                    "vespene_used_current_technology",
                    "vespene_used_current",
                    "resources_used_current",
                    "minerals_lost_army",
                    "minerals_lost_economy",
                    "minerals_lost_technology",
                    "minerals_lost",
                    "vespene_lost_army",
                    "vespene_lost_economy",
                    "vespene_lost_technology",
                    "vespene_lost",
                    "resources_lost",
                    "minerals_killed_army",
                    "minerals_killed_economy",
                    "minerals_killed_technology",
                    "minerals_killed",
                    "vespene_killed_army",
                    "vespene_killed_economy",
                    "vespene_killed_technology",
                    "vespene_killed",
                    "resources_killed",
                    "food_used",
                    "food_made",
                    "minerals_used_active_forces",
                    "vespene_used_active_forces",
                    "ff_minerals_lost_army",
                    "ff_minerals_lost_economy",
                    "ff_minerals_lost_technology",
                    "ff_vespene_lost_army",
                    "ff_vespene_lost_economy",
                    "ff_vespene_lost_technology"

            }

