from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
from config import db

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    event_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationships
    user_events = db.relationship('UserEvent', back_populates='event', cascade="all, delete-orphan")
    users = association_proxy("user_events", "user")

    def __repr__(self):
        return f"<Event #{self.id}: {self.title}>"
    
    @validates("title")
    def validate_title(self, _, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        elif len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5-50 characters")
        return title
    
    @validates("description")
    def validate_desc(self, _, desc):
        if not isinstance(desc, str):
            raise TypeError("Description must be a string")
        elif len(desc) < 80 or len(desc) > 240:
            raise ValueError("Description must be between 80-240 characters")
        return desc
    
    @validates("location")
    def validate_loc(self, _, loc):
        if not isinstance(loc, str):
            raise TypeError("Location must be a string")
        elif len(loc) < 5 or len(loc) > 50:
            raise ValueError("Location must be between 5-50 characters")
        return loc
    
    @validates("event_date")
    def validate_date(self, _, event_date):
        try:
            datetime.strptime(str(event_date), '%Y-%m-%d %H:%M')
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD HH:MM format")
        if event_date.date() < datetime.now().date():
            raise ValueError("Event cannot be in the past")
        return event_date

