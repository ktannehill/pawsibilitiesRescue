from marshmallow import fields, validate
from datetime import datetime
from models.pet import Pet
from config import ma

class PetSchema(ma.SQLAlchemySchema):

    class Meta():
        model = Pet
        load_instance = True
        fields = ("id", "image", "name", "species", "breed", "sex", "est_birthday", "age_years", "age_months", "age_weeks", "description")

    name = fields.String(required=True, 
        validate=validate.Length(min=1, max=50, error="Name must be between 1-50 characters")
    )
    species = fields.String(required=True, 
        validate=validate.Length(min=3, max=3, error="Species must be 'cat' or 'dog'")
        # {'species': ["Species must be 'cat' or 'dog' -marsh"]}
    )
    breed = fields.String(required=True, 
        validate=validate.Length(min=1, max=50, error="Breed must be between 1-50 characters")
    )
    sex = fields.String(required=True, 
        validate=validate.Length(min=3, error="Sex must be 'female' or 'male'")
    )
    description = fields.String(required=True, 
        validate=validate.Length(min=100, max=500, error="Description must be between 100-500 characters")
    )

    user = fields.Nested("UserSchema", only=("username",))

    age_years = fields.Method("get_age_years", dump_only=True)
    age_months = fields.Method("get_age_months", dump_only=True)
    age_weeks = fields.Method("get_age_weeks", dump_only=True)

    def get_age_years(self, pet):
        return self.calculate_age(pet).get("age_years")

    def get_age_months(self, pet):
        return self.calculate_age(pet).get("age_months")

    def get_age_weeks(self, pet):
        return self.calculate_age(pet).get("age_weeks")

    def calculate_age(self, pet):
        if pet.est_birthday:
            today = datetime.now().date()
            delta = today - pet.est_birthday
            years = delta.days // 365
            remaining_days = delta.days % 365
            months = remaining_days // 30
            remaining_days %= 30
            weeks = remaining_days // 7

            return {
                'age_years': years,
                'age_months': months,
                'age_weeks': weeks
            }
        return {
            'age_years': None,
            'age_months': None,
            'age_weeks': None
        }

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "petbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("pets"),
        }
    )

