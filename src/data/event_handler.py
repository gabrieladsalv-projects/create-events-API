from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.settings.connection import db_connection_handler
from src.errors.error_types.http_not_found import HttpNotFoundError
import uuid

class EventHandler:
    def __init__(self):
        with db_connection_handler as database:
            self.__events_repository = EventsRepository(session=database.session)

    
    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)

        return HttpResponse(
            body={"eventId": body["uuid"]},
            status_code=200
                            )
    

    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event = self.__events_repository.find_by_id(event_id)
        if not event: raise HttpNotFoundError("Event not found")
        
        event_attendees_count = self.__events_repository.count_event_attendees(event_id)

        return HttpResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "details": event.details,
                    "slug": event.slug,
                    "maximum_attendees": event.maximum_attendees,
                    "attendeesAmount": event_attendees_count["attendeesAmount"],
                }
            },
            status_code=200
                            )