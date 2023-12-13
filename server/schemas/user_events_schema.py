from marshmallow import fields, validate
from models.user_events import UserEvent
from config import ma

class UserEventsSchema(ma.SQLAlchemySchema):

    class Meta():
        model = UserEvent
        load_instance = True
        fields = ("user_id", "event_id")


