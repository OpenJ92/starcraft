from setup.db.raw.models.events.BasicCommandEvent import BasicCommandEvent
from setup.db.raw.models.events.ChatEvent import ChatEvent
from setup.db.raw.models.events.CameraEvent import CameraEvent
from setup.db.raw.models.events.ControlGroupEvent import ControlGroupEvent
from setup.db.raw.models.events.GetControlGroupEvent import GetControlGroupEvent

class InjectFactory():

    events = {
                BasicCommandEvent.__name__ : BasicCommandEvent,
                ChatEvent.__name__ : ChatEvent,
                CameraEvent.__name__ : CameraEvent,
                ControlGroupEvent.__name__ : ControlGroupEvent,
                GetControlGroupEvent.__name__ : GetControlGroupEvent
             }

    @classmethod
    def process(cls, replay):
        for event in replay.events:
            if event.name in cls.events.keys():
                cls.events[event.name].process(event, replay)
