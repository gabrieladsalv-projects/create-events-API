from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from src.models.entities.check_ins import CheckIns
from src.errors.error_types.http_conflict import HttpConflictError
from typing import Dict, List
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
            db_connection_handler.get_session().add(attendee)
            db_connection_handler.get_session().commit()

            return attendee_info
        except IntegrityError:
            raise HttpConflictError("Attendee already registered")
        except Exception as exception:
            db_connection_handler.get_session().rollback()
            raise exception
        
    def get_attendee_badge_by_id(self, attendee_id: str) -> Dict:
        try:
            attendee = (
                db_connection_handler.get_session()
                .query(Attendees, Events.title)
                .join(Events, Attendees.event_id == Events.id)
                .filter(Attendees.id == attendee_id)
                .with_entities(Attendees.name, Attendees.email, Events.title)
                .one()
            )
            return attendee
        except Exception as exception:
            raise exception



    def get_attendees_by_event_id(self,eventId: str) -> List[Attendees]:
        with db_connection_handler as database:
            attendees = {
                database.session
                .query(Attendees)
                .outerjoin(CheckIns, CheckIns.attendee_id == Attendees.id)
                .filter(Attendees.event_id == eventId)
                .with_entities(
                    Attendees.id,
                    Attendees.name,
                    Attendees.email,
                    CheckIns.created_at.label('check_in_at'),
                    Attendees.created_at.label('registered_at')
                )
                .all()
            }
            return attendees
            