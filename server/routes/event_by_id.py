from flask import request, abort
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from config import db
from models.event import Event
from schemas.event_schema import EventSchema

event_schema = EventSchema(session=db.session)

class EventById(Resource):
    def get(self, id):
        event = Event.query.get_or_404(
            id, description=f"Could not find event {id}"
        )
        try:
            serialized_data = event_schema.dump(event)
            return serialized_data, 200
        except Exception as e:
            abort(400, str(e))

    def patch(self, id):
        event = Event.query.get_or_404(
            id, description=f"Could not find event {id}"
        )
        try:
            data = request.get_json()
            event_schema.validate(data)
            updated_event = event_schema.load(
                data, instance=event, partial=True, session=db.session
            )
            db.session.commit()
            return event_schema.dump(updated_event), 200
        except (ValueError, ValidationError, IntegrityError) as e:
            db.session.rollback()
            abort(400, str(e))

    def delete(self, id):
        event = Event.query.get_or_404(
            id, description=f"Could not find event {id}"
        )
        try:
            db.session.delete(event)
            db.session.commit()
            return None, 204
        except Exception as e:
            db.session.rollback()
            abort(400, str(e))
