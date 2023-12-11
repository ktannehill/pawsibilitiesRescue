from flask import session
from flask_restful import Resource
from config import db
from models.user import User
from schemas.user_schema import UserSchema

user_schema = UserSchema(session=db.session)

class CheckUser(Resource): 
    def get(self):  
        if "user_id" not in session:
            return {"message": "Not authorized -CU12"}, 403
        if user := db.session.get(User, session["user_id"]):
            return user_schema.dump(user), 200
        return {"message": "Not Authorized -CU15"}, 403