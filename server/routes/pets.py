from flask import request, abort, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from config import db
from models.pet import Pet
from schemas.pet_schema import PetSchema
from models.user import User

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
        if "user_id" not in session:
            return {"message": "Not authorized"}, 403
        user = db.session.get(User, session["user_id"])
        if user.admin:
            try:
                data = request.get_json()
                pet_schema.validate(data)

                pet = pet_schema.load(data)
                db.session.add(pet)
                db.session.commit()
                return pet_schema.dump(pet), 201
            except (ValidationError, ValueError, IntegrityError) as e:
                if isinstance(e, ValidationError):
                    abort(400, [str(error[0]) for field, error in e.messages.items()][0])
                else:
                    abort(400, str(e))
        return {"message": "Not Authorized"}, 403

