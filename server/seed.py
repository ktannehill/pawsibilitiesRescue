#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from config import app, db
from models.event import Event
from models.pet import Pet
from models.user import User
from models.user_events import UserEvent

fake = Faker()

def clear_tables():
    db.drop_all()
    db.create_all()
    print("Database created!")

EVENTS = [
    {
        'title': '',
        
    }
]

def seed_events():


if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
