from flask import request, session, abort, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from flask_mail import Message
from config import db, mail, s
from schemas.user_schema import UserSchema

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
            serialized_user = user_schema.dump(user)

            token = s.dumps(user.email, salt="email-confirm")
            msg = Message(subject="Confirm Email", recipients=[user.email])
            link = f"http://127.0.0.1:4000/confirm_email/{token}"
            msg.html = f"<h2>Welcome, {user.first_name}!</h2> <p>Follow <a href={link}>this link</a> to activate your account.</p>"
            msg.content_type = "text/html"
            mail.send(msg)

            return serialized_user, 201
        except (ValidationError, ValueError, IntegrityError) as e:
            db.session.rollback()
            abort(400, str(e))

