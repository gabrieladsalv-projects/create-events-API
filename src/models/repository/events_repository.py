from src.models.settings.connection import db_handler
from src.models.entities.events import Events
from typing import Dict
from sqlalchemy.orm import Session

class EventsRepository:

    def __init__(self, session: Session) -> None:
        self.session = session

    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_handler as database:
            event = Events(
                id=eventsInfo.get("uuid"),
                title=eventsInfo.get("title"),
                details = eventsInfo.get("details"),
                slug = eventsInfo.get("slug"),
                maximum_attendees = eventsInfo.get("maximum_attendees"),
            )
            database.session.add(event)
            database.session.commit()

            return eventsInfo
        
    
    def get_event(self, event_id: str) -> Events:
        with db_handler as database:
            event = (
                database.session.query(Events)
                .filter(Events.id == event_id).one()
            )
            return event