from src.models.settings.connection import db_handler
from src.models.entities.events import Events
from typing import Dict
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class EventsRepository:

    def __init__(self, session: Session) -> None:
        self.session = session

    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_handler as database:
            try:
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
            
            except IntegrityError:
                raise Exception("Event already exists")
            except Exception as exception:
                database.session.rollback()
                raise exception
        
    
    def get_event(self, event_id: str) -> Events:
        with db_handler as database:
            try:
                event = (
                    database.session.query(Events)
                    .filter(Events.id == event_id).one()
                )
                return event
            
            except NoResultFound:
                raise Exception("Event not found")