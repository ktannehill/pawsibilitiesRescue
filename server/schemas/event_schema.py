from marshmallow import fields, validate
from datetime import datetime
from models.event import Event
from config import ma

class EventSchema(ma.SQLAlchemySchema):

    class Meta():
        model = Event
        load_instance = True
        fields = ("id", "image", "title", "description", "location", "event_date", "formatted_date_short", "formatted_date_full", "users")

    title = fields.String(required=True, 
        validate=validate.Length(min=5, max=50, error="Title must be between 5-50 characters")
    )
    description = fields.String(required=True, 
        validate=validate.Length(min=100, max=500, error="Description must be between 100-500 characters")
    )
    location = fields.String(required=True, 
        validate=validate.Length(min=5, max=50, error="Location must be between 5-50 characters")
    )

    users = fields.List(fields.Nested("UserSchema", only=("id", "username")), many=True, dump_only=True)

    formatted_date_short = fields.Method("get_formatted_date", dump_only=True)
    formatted_date_full = fields.Method("get_formatted_date_full", dump_only=True)

    def get_formatted_date(self, event):
        formatted_date = event.event_date.strftime('%-m/%-d/%y')
        formatted_time = event.event_date.strftime('%-I:%M %p').lower()
        return formatted_date + " " + formatted_time

    def get_formatted_date_full(self, event):
        formatted_date = event.event_date.strftime('%A, %B %-d, %Y')
        formatted_time = event.event_date.strftime('%-I:%M %p').lower()
        return formatted_date + " " + formatted_time
    
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "eventbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("events"),
        }
    )

