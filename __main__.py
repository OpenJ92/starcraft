import sc2reader
from sc2reader.engine.plugins import (
    SelectionTracker,
    APMTracker,
    ContextLoader,
    GameHeartNormalizer,
)

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

from os import listdir
import traceback

import argparse

parser = argparse.ArgumentParser(description="sdm : Starcraft 2 Data Project")
parser.add_argument(
    "action",
    metavar="action",
    type=str,
    help="db : run database injection \n app : run app",
)

args = parser.parse_args()

action = args.action

if action == "db":
    home = "/Users/jacob/Library/Application Support/Blizzard/StarCraft II/Accounts/91611726/1-S2-1-4635037/Replays/Multiplayer/"
    sc2Replays = listdir(home)

    for r in sc2Replays:
        if r != ".DS_Store":
            try:
                replay = sc2reader.load_replay(home + r, load_level=1)
            except Exception as e:
                traceback.print_exc()
                continue

            if INFO.process_conditions(replay):
                print(r)
                replay = sc2reader.load_replay(home + r, load_level=5)
                inject = INJECT(replay).__construct__()

elif action == "app":
    from src.app.index import *

elif action == "explore":
    events = {}
    replay = sc2reader.load_replay("example.SC2Replay", load_level=5)
    for event in replay.events:
        if event.name not in events.keys():
            events[event.name] = [event]
        else:
            events[event.name].append(event)

    def event_details(event_name, predicate=lambda e: True):
        for event in events[event_name]:
            if predicate(event):
                print(vars(event))

else:
    pass
