import sc2reader
from sc2reader.engine.plugins import SelectionTracker, APMTracker,\
        ContextLoader, GameHeartNormalizer
sc2reader.engine.register_plugin(SelectionTracker())
sc2reader.engine.register_plugin(APMTracker())
sc2reader.engine.register_plugin(ContextLoader())
sc2reader.engine.register_plugin(GameHeartNormalizer())

from src.db.raw.config import db
from src.db.raw.models.datapack.unit_type import UNIT_TYPE
from src.db.raw.models.datapack.ability import ABILITY
from src.db.raw.models.replay.info import INFO
from src.db.raw.models.replay.map import MAP
from src.db.raw.models.replay.objects import OBJECT
from src.db.raw.models.replay.player import PLAYER
from src.db.raw.inject import INJECT

from src.app.index import *
from os import listdir

## if __name__ == "__main__":
   ## home = '/Users/jacob/Library/Application Support/Blizzard/StarCraft II/Accounts/91611726/1-S2-1-4635037/Replays/Multiplayer/'
   ## sc2Replays = listdir(home)

   ## for r in sc2Replays:
   ##     if r != '.DS_Store':
   ##         print(r)
   ##         replay = sc2reader.load_replay(home+r,load_level=5,load_map=True)
   ##         inject = INJECT(replay).__construct__()

    ## events = {}
    ## for event in replay.events:
    ##     if event.name not in events.keys():
    ##         events[event.name] = [event]
    ##     else:
    ##         events[event.name].append(event)

    ## def event_details(event_name, predicate = lambda e: True):
    ##     for event in events[event_name]:
    ##         if predicate(event):
    ##             print(vars(event))
