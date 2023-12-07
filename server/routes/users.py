from flask import abort
from flask_restful import Resource
from config import db
from models.user import User
from schemas.user_schema import UserSchema

user_schema = UserSchema(session=db.session)
users_schema = UserSchema(many=True, exclude=("events",), session=db.session)

class Users(Resource):
    def get(self):
        try:
            users = users_schema.dump(User.query)
            return users, 200
        except Exception as e:
            abort(400, str(e))

