from setup.db.raw.models.events.BasicCommandEvent import BasicCommandEvent
from setup.db.raw.models.events.ChatEvent import ChatEvent

class InjectFactory():

    events = {
                BasicCommandEvent.__name__ : BasicCommandEvent,
                ChatEvent.__name__ : ChatEvent
             }

    @classmethod
    def process(cls, replay):
        for event in replay.events:
            if event.name in cls.events.keys():
                cls.events[event.name].process(event, replay)
