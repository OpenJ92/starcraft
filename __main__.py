import sc2reader
from sc2reader.engine.plugins import SelectionTracker, APMTracker,\
        ContextLoader, GameHeartNormalizer
sc2reader.engine.register_plugin(SelectionTracker())
sc2reader.engine.register_plugin(APMTracker())
sc2reader.engine.register_plugin(ContextLoader())
sc2reader.engine.register_plugin(GameHeartNormalizer())

from setup.db.raw.config import db, app

if __name__ == "__main__":
    replay = sc2reader.load_replay("example.SC2Replay", load_level=5, load_map=True)
