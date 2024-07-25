from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from typing import Dict
from src.models.entities.events import Events

class EventsRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def insert_event(self, eventsInfo: Dict) -> Dict:
        try:
            event = Events(
                id=eventsInfo.get("uuid"),
                title=eventsInfo.get("title"),
                details=eventsInfo.get("details"),
                slug=eventsInfo.get("slug"),
                maximum_attendees=eventsInfo.get("maximum_attendees"),
            )
            self.session.add(event)
            self.session.commit()
            return eventsInfo
        except IntegrityError:
            self.session.rollback()
            raise Exception("Event already exists")
        except Exception as exception:
            self.session.rollback()
            raise exception
    
    def get_event_by_id(self, event_id: str) -> Events:
        try:
            event = (
                self.session.query(Events).filter(Events.id == event_id).one()
            )
            return event
        except NoResultFound:
            return None
        
    
    def count_event_attendees(self, event_id:str) -> Dict:
        with db_connection_handler as database:
            event_count = (
                database.session.query(Events).join(Attendees, Events.id == Attendees.event_id).filter(Events.id == event_id).with_entities(Events.maximum_attendees, Attendees.id)
                ).all()
            if not len(event_count):
                return {
                    "maximum_attendees": 0,
                    "attendeesAmount": 0
                }
                return {
                    "maximum_attendees": event_count[0].maximum_attendees,
                    "attendeesAmount": len(event_count)
                }
