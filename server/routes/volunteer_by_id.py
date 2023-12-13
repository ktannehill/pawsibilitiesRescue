from flask import request, session, abort
from flask_restful import Resource
from config import db
from models.user_events import UserEvent
from schemas.user_events_schema import UserEventsSchema

user_events_schema = UserEventsSchema(session=db.session)

class UserEventById(Resource):
    def delete(self, id):
        try:
            user_id = session['user_id']
            user_event = UserEvent.query.filter_by(user_id=user_id, event_id=id).first()

            if user_event:
                db.session.delete(user_event)
                db.session.commit()
                return {}, 201
            else:
                return {'message': f'User {id} is not signed up for event {id}'}, 400

        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 400