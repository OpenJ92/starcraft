from src.db.raw.models.datapack.ability import ABILITY 
from src.db.raw.models.datapack.unit_type import UNIT_TYPE

from src.db.raw.models.replay.player import PLAYER
from src.db.raw.models.replay.objects import OBJECT
from src.db.raw.models.replay.info import INFO
from src.db.raw.models.replay.map import MAP

from src.db.raw.models.events.BasicCommandEvent import BasicCommandEvent
from src.db.raw.models.events.ChatEvent import ChatEvent
from src.db.raw.models.events.CameraEvent import CameraEvent
from src.db.raw.models.events.ControlGroupEvent import ControlGroupEvent
from src.db.raw.models.events.GetControlGroupEvent import GetControlGroupEvent
from src.db.raw.models.events.SetControlGroupEvent import SetControlGroupEvent
from src.db.raw.models.events.PlayerStatsEvent import PlayerStatsEvent
from src.db.raw.models.events.PlayerLeaveEvent import PlayerLeaveEvent
from src.db.raw.models.events.PlayerSetupEvent import PlayerSetupEvent
from src.db.raw.models.events.TargetPointCommandEvent import TargetPointCommandEvent
from src.db.raw.models.events.TargetUnitCommandEvent import TargetUnitCommandEvent
from src.db.raw.models.events.UpgradeCompleteEvent import UpgradeCompleteEvent 
from src.db.raw.models.events.UnitBornEvent import UnitBornEvent
from src.db.raw.models.events.UnitDoneEvent import UnitDoneEvent
from src.db.raw.models.events.UnitInitEvent import UnitInitEvent
from src.db.raw.models.events.UnitTypeChangeEvent import UnitTypeChangeEvent
from src.db.raw.models.events.UnitPositionsEvent import UnitPositionsEvent
from src.db.raw.models.events.SelectionEvent import SelectionEvent
from src.db.raw.models.events.UnitDiedEvent import UnitDiedEvent

from src.db.raw.config import db 

if __name__ == "__main__":
    db.create_all()
