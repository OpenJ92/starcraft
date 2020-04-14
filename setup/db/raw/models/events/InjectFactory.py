from setup.db.raw.models.events.BasicCommandEvent import BasicCommandEvent
from setup.db.raw.models.events.ChatEvent import ChatEvent

class InjectFactory():

    events = {
                BasicCommandEvent.__name__ : BasicCommandEvent
                ChatEvent.__name__ : ChatEvent
             }

    def process(replay):
        for event in replay.events:
            cls.events[event.name].process(event, replay)

