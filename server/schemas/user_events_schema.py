from marshmallow import fields, validate, validates, ValidationError
from models.user_events import UserEvent
from config import ma

class UserEventSchema(ma.SQLAlchemySchema):
    class Meta():
        model = UserEvent
        load_instance = True
        fields = ("user_id", "event_id")