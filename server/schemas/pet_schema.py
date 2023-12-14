from marshmallow import fields, validate
from models.pet import Pet
from config import ma

class PetSchema(ma.SQLAlchemySchema):

    class Meta():
        model = Pet
        load_instance = True
        fields = ("id", "image", "name", "species", "breed", "sex", "est_birthday", "description")

    name = fields.String(required=True, 
        validate=validate.Length(min=1, max=50, error="Name must be between 1-50 characters")
    )
    species = fields.String(required=True, 
        validate=validate.Length(min=3, max=3, error="Species must be 'cat' or 'dog'")
    )
    breed = fields.String(required=True, 
        validate=validate.Length(min=1, max=50, error="Breed must be between 1-50 characters")
    )
    sex = fields.String(required=True, 
        validate=validate.Length(min=3, error="Sex must be 'female' or 'male'")
    )
    description = fields.String(required=True, 
        validate=validate.Length(min=160, max=480, error="Description must be between 160-480 characters")
    )

    user = fields.Nested("UserSchema", only=("username",))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "petbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("pets"),
        }
    )

