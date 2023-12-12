from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
import re
from config import db, bcrypt

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    confirmed = db.Column(db.Boolean, server_default="0")
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationships
    pets = db.relationship("Pet", back_populates="user")
    user_events = db.relationship('UserEvent', back_populates='user', cascade="all, delete-orphan")
    events = association_proxy("user_events", "event")

    def __repr__(self):
        return f"<User #{self.id}: {self.username}>"
    
    @validates("first_name")
    def validate_first(self, _, first):
        if not isinstance(first, str):
            raise TypeError("First name must be a string")
        elif len(first) < 1 or len(first) > 50:
            raise ValueError("First name must be between 1-50 characters")
        return first
    
    @validates("last_name")
    def validate_last(self, _, last):
        if not isinstance(last, str):
            raise TypeError("Last name must be a string")
        elif len(last) < 1 or len(last) > 50:
            raise ValueError("Last name must be between 1-50 characters")
        return last
    
    @validates("username")
    def validate_username(self, _, username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        elif len(username) < 5 or len(username) > 50:
            raise ValueError("Username must be between 5-50 characters")
        elif not re.match(r"^[a-zA-Z0-9_-]+$", username):
            raise ValueError("Usernames may only contain alphanumeric characters, dashes(-), or underscores(_)")
        return username

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Passwords are not to be shared")
    
    @password_hash.setter
    def password_hash(self, new_pass):
        hashed_pass = bcrypt.generate_password_hash(new_pass).decode("utf-8")
        self._password_hash = hashed_pass

    def authenticate(self, pass_to_check):
        return bcrypt.check_password_hash(self._password_hash, pass_to_check)
