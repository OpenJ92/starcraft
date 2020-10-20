from src.db.raw.models.events.InjectFactory import InjectFactory
from src.db.raw.models.replay.replayInjectFactory import replayInjectFactory
from src.db.raw.models.datapack.datapackInjectFactory import datapackInjectFactory

class INJECT():
    def __init__(self, replay):
        self._replay = replay

    def __construct__(self):
        if replayInjectFactory.predicate.process_conditions(self._replay):
            datapackInjectFactory.process(self._replay)
            replayInjectFactory.process(self._replay)
            InjectFactory.process(self._replay)
