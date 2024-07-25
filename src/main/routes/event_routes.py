from flask import Blueprint, request, jsonify
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler


event_route_bp = Blueprint('event_route', __name__)


@event_route_bp.route('/events', methods=['POST'])
def create_event():
    http_request = HttpRequest(body=request.json)
    event_handler = EventHandler()

    http_response = event_handler.register(http_request)
    try:
        return jsonify(http_response.body), http_response.status_code
    except Exception:
        return jsonify({'message': 'Error creating event'}, 500)
    

@event_route_bp.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    http_request = HttpRequest(param={'event_id': event_id})
    event_handler = EventHandler()

    http_response = event_handler.get(http_request)
    try:
        return jsonify(http_response.body), http_response.status_code
    except Exception:
        return jsonify({'message': 'Error getting event'}, 500)