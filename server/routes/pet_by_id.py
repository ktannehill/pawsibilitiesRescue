from flask import request, abort
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from datetime import datetime
from config import db
from models.pet import Pet
from schemas.pet_schema import PetSchema

pet_schema = PetSchema(session=db.session)

class PetById(Resource):
    def get(self, id):
        pet = Pet.query.get_or_404(
            id, description=f"Could not find pet {id}"
        )
        try:
            pet.calculate_age()
            serialized_data = pet_schema.dump(pet)
            return serialized_data, 200
        except Exception as e:
            abort(400, str(e))

    def patch(self, id):
        pet = Pet.query.get_or_404(
            id, description=f"Could not find pet {id}"
        )
        try:
            data = request.get_json()
            pet_schema.validate(data)

            # if est_birthday_str := data.get("est_birthday"):
            #     data["est_birthday"] = datetime.strptime(est_birthday_str, '%Y-%m-%d').date()

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
        try:
            db.session.delete(pet)
            db.session.commit()
            return None, 204
        except Exception as e:
            db.session.rollback()
            abort(400, str(e))
