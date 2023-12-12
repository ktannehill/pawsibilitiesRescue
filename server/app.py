#!/usr/bin/env python3

# Standard/ Remote library imports
from werkzeug.exceptions import NotFound
from itsdangerous import SignatureExpired

# Local imports
from config import app, api, db, s
# Add your model imports
from models.event import Event
from models.pet import Pet
from models.user import User
from models.user_events import UserEvent

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

@app.errorhandler(NotFound)
def handle_404(error):
    response = {"message": error.description}
    return response, error.code

@app.route("/confirm_email/<token>")
def confirm_email(token):
    try:
        email = s.loads(token, salt="email-confirm", max_age=600)
        user = User.query.filter_by(email=email).first()
        user.confirmed = True
        db.session.commit()
        return 

    except SignatureExpired:
        return {"message": "Token expired"}, 400
    return 


if __name__ == '__main__':
    app.run(port=5555, debug=True)

