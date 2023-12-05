from . import validates
from config import db
from user import User
from event import Event

class UserEvent(db.Model):
    __tablename__ = "user_events"

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), primary_key=True)
    created_at = db.Column(db.Datetime, server_default=db.func.now())
    updated_at = db.Column(db.Datetime, onupdate=db.func.now())

    # relationships
    user = db.relationship('User', back_populates='user_events')
    event = db.relationship('Event', back_populates='user_events')

    def __repr__(self):
        return f"<UserEvent #{self.user_id}-{self.event_id}>"
    
    @validates("user_id")
    def validate_user_id(self, _, user_id):
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer")
        elif not db.session.get(User, user_id):
            raise ValueError("User does not exist")
        return user_id

    @validates("event_id")
    def validate_event_id(self, _, event_id):
        if not isinstance(event_id, int):
            raise ValueError("Event ID must be an integer")
        elif not db.session.get(Event, event_id):
            raise ValueError("Event does not exist")
        return event_id