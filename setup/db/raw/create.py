from setup.db.raw.models.datapack.ability import ABILITY 
from setup.db.raw.models.datapack.unit_type import UNIT_TYPE

from setup.db.raw.models.replay.player import PLAYER
from setup.db.raw.models.replay.objects import OBJECT
from setup.db.raw.models.replay.info import INFO
from setup.db.raw.models.replay.map import MAP

from setup.db.raw.models.events.BasicCommandEvent import BasicCommandEvent
from setup.db.raw.models.events.ChatEvent import ChatEvent

from setup.db.raw.config import db 

db.create_all()
