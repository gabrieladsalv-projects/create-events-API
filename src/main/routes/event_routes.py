from flask import Blueprint, request, jsonify
from src.http_types.http_request import HttpRequest

event_route_bp = Blueprint('event_route', __name__)


@event_route_bp.route('/events', methods=['POST'])
def create_event():
    request = HttpRequest(body=request.json)
    return jsonify({'message': 'Event created'}), 200