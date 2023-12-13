from flask import request, session, abort
from flask_restful import Resource
from config import db
from models.user_events import UserEvent
from schemas.user_events_schema import UserEventsSchema

user_events_schema = UserEventsSchema(session=db.session)

class UserEvents(Resource):
    def post(self):
        if 'user_id' not in session:
            return {'error': 'User not logged in'}, 401

        user_id = session['user_id']
        event_id = int(request.json.get('event_id'))

        print(user_id, event_id)

        user_event = UserEvent.query.filter_by(user_id=user_id, event_id=event_id).first()
        if user_event:
            return {'message': 'You already volunteered for this event!'}, 400

        try:
            new_ue = UserEvent(user_id=user_id, event_id=event_id)
            db.session.add(new_ue)
            db.session.commit()
            print(new_ue)
            return user_events_schema.dump(new_ue), 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 400