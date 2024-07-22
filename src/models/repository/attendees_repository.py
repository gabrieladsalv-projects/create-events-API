from src.models.settings.connection import db_handler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from typing import Dict
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class AttendeesRepository:
    def insert_attendee(self, attendee_info: Dict) -> Dict:
        try:
            attendee = Attendees(
                id=attendee_info.get('uuid'),
                name=attendee_info.get('name'),
                email=attendee_info.get('email'),
                event_id=attendee_info.get('event_id')
            )
            db_handler.get_session().add(attendee)
            db_handler.get_session().commit()

            return attendee_info
        except IntegrityError:
            raise Exception("Attendee already registered")
        except Exception as exception:
            db_handler.get_session().rollback()
            raise exception
        
    def get_attendee_badge_by_id(self, attendee_id: str) -> Dict:
        try:
            attendee = (
                db_handler.get_session()
                .query(Attendees, Events.title)
                .join(Events, Attendees.event_id == Events.id)
                .filter(Attendees.id == attendee_id)
                .with_entities(Attendees.name, Attendees.email, Events.title)
                .one()
            )
            return attendee
        except Exception as exception:
            raise exception
