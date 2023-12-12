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

            print("SU29: ", serialized_user)

            token = s.dumps(user.email, salt="email-confirm")
            msg = Message(subject="Confirm Email", sender="pawsibilitiesrescueproject@gmail.com", recipients=[user.email])
            link = url_for("confirm_email", token=token, _external=True)
            msg.body = f"<h2>Welcome, {user.first_name}!</h2> <p>Your confirmation link is {link}</p>"
            mail.send(msg)

            return {"user": serialized_user, "requiresConfirmation": True}, 201
        except (ValidationError, ValueError, IntegrityError) as e:
            db.session.rollback()
            abort(400, str(e))

