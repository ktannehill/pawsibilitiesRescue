from flask import request, abort
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from datetime import datetime
from config import db
from models.pet import Pet
from schemas.pet_schema import PetSchema

pet_schema = PetSchema(session=db.session)
pets_schema = PetSchema(many=True, session=db.session)

class Pets(Resource):
    def get(self):
        try:
            pets = pets_schema.dump(Pet.query)
            return pets, 200
        except Exception as e:
            abort(400, str(e))

    def post(self):
        try:
            data = request.get_json()
            pet_schema.validate(data)

            # if est_birthday_str := data.get("est_birthday"):
            #     data["est_birthday"] = datetime.strptime(est_birthday_str, '%Y-%m-%d').date()

            pet = pet_schema.load(data)
            db.session.add(pet)
            import ipdb; ipdb.set_trace()
            db.session.commit()
            serialized_pet = pet_schema.dump(pet)
            return serialized_pet, 201
        except (ValidationError, ValueError, IntegrityError) as e:
            db.session.rollback()
            abort(400, str(e))

