from datetime import datetime
from . import validates
from config import db

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    breed = db.Column(db.String, nullable=False)
    est_birthday = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.Datetime, server_default=db.func.now())
    updated_at = db.Column(db.Datetime, onupdate=db.func.now())

    # relationships

    def __repr__(self):
        return f"<Pet #{self.id}: {self.name}>"
    
    @validates("name")
    def validate_name(self, _, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        elif len(name) < 1 or len(name) > 50:
            raise ValueError("Name must be between 1-50 characters")
        return name
    
    @validates("species")
    def validate_species(self, _, species):
        if not isinstance(species, str):
            raise TypeError("Species must be a string")
        elif species.lower() not in ["cat", "dog"]:
            raise ValueError("Species must be 'cat' or 'dog'")
        return species
    
    @validates("breed")
    def validate_breed(self, _, breed):
        if not isinstance(breed, str):
            raise TypeError("Breed must be a string")
        elif len(breed) < 1 or len(breed) > 50:
            raise ValueError("Breed must be between 1-50 characters")
        return breed
    
    @validates("est_birthday")
    def validate_birthday(self, _, birthday):
        if not isinstance(birthday, datetime):
            raise TypeError("Birthday must be in datetime")
        elif birthday.date() > datetime.now().date():
            raise ValueError("Birthday cannot be in the future")
        return birthday
    
    @validates("description")
    def validate_desc(self, _, desc):
        if not isinstance(desc, str):
            raise TypeError("Description must be a string")
        elif len(desc) < 160 or len(desc) > 480:
            raise ValueError("Description must be between 160-480 characters")
        return desc

    def calculate_age(self):
        if self.est_birthday:
            today = datetime.now().date()
            age = today.year - self.est_birthday.year - (
                (today.month, today.day) < (self.est_birthday.month, self.est_birthday.day)
            )
            return age
        return None
