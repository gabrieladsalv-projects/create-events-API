import pytest
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.settings.connection import db_handler

@pytest.fixture(scope="module")
def setup_database():
    db_handler.connect_to_db()
    yield
    db_handler.close_session()

@pytest.mark.usefixtures("setup_database")
def test_insert_attendee():
    event_id = '123'
    attendees_info = {
        'uuid': 'attendee_uuid',
        'name': 'attendee name',
        'email': 'attendee_email@email.com',
        'event_id': event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    assert response == attendees_info


@pytest.mark.skip(reason="Integrity Test not implemented")
def test_get_attendee_badge_by_id():
    attendee_id = "attendee_uuid"
    attendees_repository = AttendeesRepository()
    attendee_info = attendees_repository.get_attendee_badge_by_id(attendee_id)
    print(attendee_info)

