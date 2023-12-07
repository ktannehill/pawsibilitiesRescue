from marshmallow import fields, validate
from models.event import Event
from config import ma

class EventSchema(ma.SQLAlchemySchema):

    class Meta():
        model = Event
        load_instance = True
        fields = ("id", "image", "title", "description", "location", "event_date", "users")

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

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "eventbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("events"),
        }
    )

