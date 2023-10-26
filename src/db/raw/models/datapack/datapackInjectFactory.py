from src.db.raw.models.datapack.ability import ABILITY
from src.db.raw.models.datapack.unit_type import UNIT_TYPE


class datapackInjectFactory:
    @classmethod
    def process(cls, replay):
        UNIT_TYPE.process(replay)
        ABILITY.process(replay)
