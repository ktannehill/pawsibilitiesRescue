from flask import request, abort
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from config import db
from models.user import User
from schemas.user_schema import UserSchema

user_schema = UserSchema(session=db.session)

class UserById(Resource):
    def get(self, id):
        user = User.query.get_or_404(
            id, description=f"Could not find user {id}"
        )
        try:
            serialized_data = user_schema.dump(user)
            return serialized_data, 200
        except Exception as e:
            abort(400, str(e))

    def patch(self, id):
        user = User.query.get_or_404(
            id, description=f"Could not find user {id}"
        )
        try:
            data = request.get_json()
            user_schema.validate(data)
            updated_user = user_schema.load(
                data, instance=user, partial=True, session=db.session
            )
            db.session.commit()
            return user_schema.dump(updated_user), 200
        except IntegrityError as e:
            # (sqlite3.IntegrityError) UNIQUE constraint failed:
            db.session.rollback()
            return {"message": "Email or username already in use"}, 400
        except (ValidationError, ValueError) as e:
            db.session.rollback()
            abort(400, str(e))

    def delete(self, id):
        user = User.query.get_or_404(
            id, description=f"Could not find user {id}"
        )
        try:
            db.session.delete(user)
            db.session.commit()
            return None, 204
        except Exception as e:
            db.session.rollback()
            abort(400, str(e))
