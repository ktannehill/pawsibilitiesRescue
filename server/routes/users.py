from flask import abort, session
from flask_restful import Resource
from config import db
from models.user import User
from schemas.user_schema import UserSchema

user_schema = UserSchema(session=db.session)
users_schema = UserSchema(many=True, exclude=("events",), session=db.session)

class Users(Resource):
    def get(self):
        if "user_id" not in session:
            return {"message": "Not authorized"}, 403
        user = db.session.get(User, session["user_id"])
        if user.admin:
            try:
                users = users_schema.dump(User.query)
                return users, 200
            except Exception as e:
                abort(400, str(e))
        return {"message": "Not Authorized"}, 403

