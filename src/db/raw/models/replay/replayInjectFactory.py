from src.db.raw.models.replay.player import PLAYER
from src.db.raw.models.replay.objects import OBJECT
from src.db.raw.models.replay.info import INFO
from src.db.raw.models.replay.map import MAP

class replayInjectFactory():
    predicate = INFO

    @classmethod
    def process(cls, replay):
        if replay.map: MAP.process(replay)
        INFO.process(replay)
        PLAYER.process(replay)
        OBJECT.process(replay)
