#!/usr/bin/env python3

# Standard/ Remote library imports
from werkzeug.exceptions import NotFound
from flask import session
from flask_mail import Message
from itsdangerous import SignatureExpired, BadSignature

# Local imports
from config import app, api, db, mail, s
# Add your model imports
from models.event import Event
from models.pet import Pet
from models.user import User
from models.user_events import UserEvent

from schemas.user_schema import UserSchema

from routes.users import Users
from routes.user_by_id import UserById
from routes.events import Events
from routes.event_by_id import EventById
from routes.pets import Pets
from routes.pet_by_id import PetById
from routes.auth.signup import Signup
from routes.auth.login import Login
from routes.auth.logout import Logout
from routes.auth.check_user import CheckUser
from routes.volunteer import UserEvents
from routes.volunteer_by_id import UserEventById
from utilities import send_confirmation_email

user_schema = UserSchema(session=db.session)

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:id>")
api.add_resource(Events, "/events")
api.add_resource(EventById, "/events/<int:id>")
api.add_resource(Pets, "/pets")
api.add_resource(PetById, "/pets/<int:id>")
api.add_resource(Signup, "/signup")
api.add_resource(Login, "/user_login")
api.add_resource(Logout, "/logout")
api.add_resource(CheckUser, "/check_user")
api.add_resource(UserEvents, "/volunteer")
api.add_resource(UserEventById, "/volunteer_by_id/<int:id>")

@app.errorhandler(NotFound)
def handle_404(error):
    response = {"message": error.description}
    return response, error.code

@app.route("/resend_confirmation_email/<int:user_id>")
def resend_confirmation_email(user_id):
    user = User.query.get(user_id)
    if user:
        send_confirmation_email(user)
        return {"user": user_schema.dump(user)}, 200
    else:
        return {"message": "User not found"}, 404

@app.route("/confirm_email/<token>")
def confirm_email(token, expiration=30):
    try:
        email = s.loads(token, salt="email-confirm", max_age=expiration)
    except SignatureExpired:
        return {"message": "Token expired"}, 400
    except BadSignature:
        return {"message": "Invalid token"}, 400
    if user := User.query.filter_by(email=email).first():
        user.confirmed = True
        db.session.commit()
        return {"user": user_schema.dump(user)}, 200
    return {"message": "No matching user found"}, 400

@app.route("/event_confirmation_email/<int:id>")
def event_confirmation_email(id):
    print(id)
    if "user_id" not in session:
            return {"message": "Not authorized"}, 403
    if user := db.session.get(User, session["user_id"]):
        print(user)
        event = db.session.get(Event, id)
        print(event)
        msg = Message(subject="Volunteer Confirmation", recipients=[user.email])
        msg.html = (f"<h2>Thanks for signing up for {event.title}!</h2>" 
            f"<p>Location: {event.location}</p>"
            f"<p>Date: {event.event_date}</p>"
            f"<p>Description: {event.description}</p>")
        msg.content_type = "text/html"
        mail.send(msg)
        return {"user": user_schema.dump(user)}, 200
    return {"message": "Not Authorized"}, 403


if __name__ == '__main__':
    app.run(port=5555, debug=True)

