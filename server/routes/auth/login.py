from flask import request, session
from flask_restful import Resource
from config import db
from models.user import User
from schemas.user_schema import UserSchema

user_schema = UserSchema(session=db.session)

class Login(Resource): 
    def post(self): 
        try:
            data = request.get_json()
            user_by_username = User.query.filter_by(username = data.get('username')).first()
            user_by_email = User.query.filter_by(email = data.get('username')).first()

            if (user_by_username or user_by_email):
                user = user_by_username or user_by_email
                if user.authenticate(data.get('password')):
                    session['user_id'] = user.id
                    return user_schema.dump(user), 200
            return {'message': 'Invalid credentials'}, 403
        except Exception as e:
            return {'message': 'Invalid credentials'}, 403