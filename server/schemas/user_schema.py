from marshmallow import fields, validates, validate, ValidationError
from models.user import User
from schemas.user_events_schema import UserEventSchema
from config import ma

class UserSchema(ma.SQLAlchemySchema):

    class Meta():
        model = User
        load_instance = True
        fields = ("id", "first_name", "last_name", "username", "email")

    first_name = fields.String(required=True, 
        validate=validate.Length(min=1, max=50, error="First name must be between 1-50 characters")
    )
    last_name = fields.String(required=True, 
        validate=validate.Length(min=1, max=50, error="Last name must be between 1-50 characters")
    )
    username = fields.String(required=True, 
        validate=validate.Length(min=5, max=50, error="Username must be between 5-50 characters")
    )

    # events = fields.Nested("EventSchema", exclude=("users",), many=True, dump_only=True)
    user_events = fields.List(fields.Nested(UserEventSchema))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "userbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("users"),
        }
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)