from flask import request, abort, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from config import db
from models.pet import Pet
from schemas.pet_schema import PetSchema
from models.user import User

pet_schema = PetSchema(session=db.session)

class PetById(Resource):
    def get(self, id):
        pet = Pet.query.get_or_404(
            id, description=f"Could not find pet {id}"
        )
        try:
            serialized_data = pet_schema.dump(pet)
            return serialized_data, 200
        except Exception as e:
            abort(400, str(e))

    def patch(self, id):
        pet = Pet.query.get_or_404(
            id, description=f"Could not find pet {id}"
        )
        if "user_id" not in session:
            return {"message": "Not authorized"}, 403
        user = db.session.get(User, session["user_id"])
        if user.admin:
            try:
                data = request.get_json()
                pet_schema.validate(data)

                updated_pet = pet_schema.load(
                    data, instance=pet, partial=True, session=db.session
                )
                db.session.commit()
                return pet_schema.dump(updated_pet), 200
            except (ValueError, ValidationError, IntegrityError) as e:
                db.session.rollback()
                abort(400, str(e))

    def delete(self, id):
        pet = Pet.query.get_or_404(
            id, description=f"Could not find pet {id}"
        )
        if "user_id" not in session:
            return {"message": "Not authorized"}, 403
        user = db.session.get(User, session["user_id"])
        if user.admin:
            try:
                db.session.delete(pet)
                db.session.commit()
                return None, 204
            except Exception as e:
                db.session.rollback()
                abort(400, str(e))
        return {"message": "Not Authorized"}, 403
