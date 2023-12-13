from flask import request, session, abort, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from config import db
from schemas.user_schema import UserSchema
from utilities import send_confirmation_email

user_schema = UserSchema(session=db.session)

class Signup(Resource): 
    def post(self):
        try:
            data = {
                "first_name": request.get_json().get("first_name"),
                "last_name": request.get_json().get("last_name"),
                "username": request.get_json().get("username"),
                "email": request.get_json().get("email"),
            }
            user_schema.validate(data)
            user = user_schema.load(data)
            user.confirmed = False
            user.password_hash = request.get_json().get("password")
            db.session.add(user)
            db.session.commit()
            session["user_id"] = user.id

            send_confirmation_email(user)

            return user_schema.dump(user), 201
        except (ValidationError, ValueError, IntegrityError) as e:
            db.session.rollback()
            abort(400, str(e))

