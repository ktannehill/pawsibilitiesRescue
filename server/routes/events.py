from flask import request, abort
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from datetime import datetime
from config import db
from models.event import Event
from schemas.event_schema import EventSchema

event_schema = EventSchema(session=db.session)
events_schema = EventSchema(many=True, session=db.session)

class Events(Resource):
    def get(self):
        try: 
            events = events_schema.dump(Event.query)
            return events, 200
        except Exception as e:
            abort(400, str(e))

    def post(self):
        try:
            data = request.get_json()
            event_schema.validate(data)
            event = event_schema.load(data)
            db.session.add(event)
            db.session.commit()
            serialized_event = event_schema.dump(event)
            return serialized_event, 201
        except (ValidationError, ValueError, IntegrityError) as e:
            db.session.rollback()
            abort(400, str(e))

