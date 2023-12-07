#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from werkzeug.exceptions import NotFound

# Local imports
from config import app, db, api
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
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(CheckUser, "/check_user")

@app.errorhandler(NotFound)
def handle_404(error):
    response = {"message": error.description}
    return response, error.code


if __name__ == '__main__':
    app.run(port=5555, debug=True)

