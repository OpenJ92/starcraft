from setup.db.raw.models.datapack.ability import ABILITY 
from setup.db.raw.models.datapack.unit_type import UNIT_TYPE
from setup.db.raw.models.replay.player import PLAYER
from setup.db.raw.models.replay.objects import OBJECT
from setup.db.raw.models.replay.info import INFO
from setup.db.raw.models.replay.map import MAP

from setup.db.raw.models.events.InjectFactory import InjectFactory

class INJECT():
    def __init__(self, replay):
        self._replay = replay

    def __construct__(self):
        if INFO.process_conditions(self._replay):
            UNIT_TYPE.process(self._replay)
            ABILITY.process(self._replay)
            MAP.process(self._replay)
            INFO.process(self._replay)
            PLAYER.process(self._replay)
            OBJECT.process(self._replay)

            InjectFactory.process(self._replay)
