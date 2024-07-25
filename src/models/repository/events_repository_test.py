import pytest
from src.models.settings.connection import db_connection_handler
from src.models.repository.events_repository import EventsRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="New register in database")
def test_insert_event():
 
        
        event = {
            "uuid": "123",
            "title": "Test Event",
            "details": "This is a test event",
            "slug": "test-event",
            "maximum_attendees": 100
        }
        
        events_repository = EventsRepository(session=db_connection_handler.session)
        response = events_repository.insert_event(event)
        
        print(response)


@pytest.mark.skip(reason="Not necessary")
def test_get_event_by_id():
    event_id = "123"
    events_repository = EventsRepository(session=db_connection_handler.session)
    response = events_repository.get_event(event_id)
    print(response)
