from setup.db.raw.models.events.BasicCommandEvent import BasicCommandEvent
from setup.db.raw.models.events.ChatEvent import ChatEvent
from setup.db.raw.models.events.CameraEvent import CameraEvent
from setup.db.raw.models.events.ControlGroupEvent import ControlGroupEvent
from setup.db.raw.models.events.GetControlGroupEvent import GetControlGroupEvent
from setup.db.raw.models.events.SetControlGroupEvent import SetControlGroupEvent
from setup.db.raw.models.events.PlayerStatsEvent import PlayerStatsEvent
from setup.db.raw.models.events.PlayerLeaveEvent import PlayerLeaveEvent
from setup.db.raw.models.events.PlayerSetupEvent import PlayerSetupEvent
from setup.db.raw.models.events.TargetPointCommandEvent import TargetPointCommandEvent
from setup.db.raw.models.events.TargetUnitCommandEvent import TargetUnitCommandEvent
from setup.db.raw.models.events.UpgradeCompleteEvent import UpgradeCompleteEvent 

class InjectFactory():

    events = {
                BasicCommandEvent.__name__ : BasicCommandEvent,
                ChatEvent.__name__ : ChatEvent,
                CameraEvent.__name__ : CameraEvent,
                ControlGroupEvent.__name__ : ControlGroupEvent,
                GetControlGroupEvent.__name__ : GetControlGroupEvent,
                SetControlGroupEvent.__name__ : SetControlGroupEvent,
                PlayerStatsEvent.__name__ : PlayerStatsEvent,
                PlayerLeaveEvent.__name__ : PlayerLeaveEvent,
                PlayerSetupEvent.__name__ : PlayerSetupEvent,
                TargetPointCommandEvent.__name__ : TargetPointCommandEvent,
                TargetUnitCommandEvent.__name__ : TargetUnitCommandEvent,
                UpgradeCompleteEvent .__name__ : UpgradeCompleteEvent 
             }

    @classmethod
    def process(cls, replay):
        for event in replay.events:
            if event.name in cls.events.keys():
                cls.events[event.name].process(event, replay)
