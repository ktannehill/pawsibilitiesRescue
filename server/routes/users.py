from flask import request, abort
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from config import db
from models.user import User
from schemas.user_schema import UserSchema

user_schema = UserSchema(session=db.session)
users_schema = UserSchema(many=True, exclude=("events", "pets"), session=db.session)

class Users(Resource):
    def get(self):
        try:
            users = users_schema.dump(User.query)
            return users, 200
        except Exception as e:
            abort(400, str(e))

    def post(self):
        try:
            data = request.get_json()
            user_schema.validate(data)
            user = user_schema.load(data)
            db.session.add(user)
            db.session.commit()
            serialized_user = user_schema.dump(user)
            return serialized_user, 201
        except (ValidationError, ValueError, IntegrityError) as e:
            db.session.rollback()
            abort(400, str(e))

