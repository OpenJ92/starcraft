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


class InjectFactory:
    events = {
        BasicCommandEvent.__name__: BasicCommandEvent,
        ChatEvent.__name__: ChatEvent,
        CameraEvent.__name__: CameraEvent,
        ControlGroupEvent.__name__: ControlGroupEvent,
        GetControlGroupEvent.__name__: GetControlGroupEvent,
        SetControlGroupEvent.__name__: SetControlGroupEvent,
        PlayerStatsEvent.__name__: PlayerStatsEvent,
        PlayerLeaveEvent.__name__: PlayerLeaveEvent,
        PlayerSetupEvent.__name__: PlayerSetupEvent,
        TargetPointCommandEvent.__name__: TargetPointCommandEvent,
        TargetUnitCommandEvent.__name__: TargetUnitCommandEvent,
        UpgradeCompleteEvent.__name__: UpgradeCompleteEvent,
        UnitBornEvent.__name__: UnitBornEvent,
        UnitDoneEvent.__name__: UnitDoneEvent,
        UnitInitEvent.__name__: UnitInitEvent,
        UnitTypeChangeEvent.__name__: UnitTypeChangeEvent,
        UnitPositionsEvent.__name__: UnitPositionsEvent,
        SelectionEvent.__name__: SelectionEvent,
        UnitDiedEvent.__name__: UnitDiedEvent,
    }

    @classmethod
    def process(cls, replay):
        for event in replay.events:
            if event.name in cls.events.keys():
                cls.events[event.name].process(event, replay)
