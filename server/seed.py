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
    # {
    #     'image': "",
    #     'title': "",
    #     'description': "",
    #     'location': "",
    #     'event_date': "",
    # },
    {
        'image': "",
        'title': "Paws in the Park Cleanup",
        'description': "Join us for a community park cleanup to create a safe and enjoyable space for our furry friends. We'll be clearing trails, picking up trash, and ensuring a clean environment for pets and their owners.",
        'location': "City Park, Denver",
        'event_date': "2024-03-10 09:00",
    },
    {
        'image': "",
        'title': "Adoption Day Extravaganza",
        'description': "Help us set up and organize our biggest adoption event of the year! Assist with booth setup, guide potential adopters, and create a welcoming atmosphere for our rescue animals.",
        'location': "Paw-sibilities Rescue Center",
        'event_date': "2024-04-15 11:00",
    },
    {
        'image': "",
        'title': "Feline Friends Socialization Hour",
        'description': "Spend quality time with our adorable cats awaiting adoption. Engage in playtime, offer companionship, and help socialize our feline friends to improve their chances of finding forever homes.",
        'location': "Kitty Cuddle Haven, Denver",
        'event_date': "2024-05-05 03:00",
    },
    {
        'image': "",
        'title': "Dog Walking Adventure Group",
        'description': "Grab a leash and join us for a scenic dog walking adventure in the beautiful local trails. It's a great opportunity to exercise, enjoy nature, and provide our rescue dogs with much-needed outdoor time.",
        'location': "Local Trails, Denver",
        'event_date': "2024-06-20 10:00",
    },
    {
        'image': "",
        'title': "Pet Picture Day",
        'description': "Join us for a fun-filled day of capturing special moments with your beloved pets! Bring your furry friends to the local park, and our professional photographers will be on hand to take beautiful pictures. Cherish the memories forever!",
        'location': "Washington Park, Denver",
        'event_date': "2024-03-18 02:00",
    },
    {
        'image': "",
        'title': "Senior Dogs Pup Cups",
        'description': "Treat your senior dogs to a delightful outing! We'll be taking our senior furry friends to Starbucks, where they can enjoy pup cups and receive lots of love. It's a heartwarming experience for both the dogs and their human companions!",
        'location': "Starbucks on ",
        'event_date': "2024-05-23 04:00",
    },
]

def seed_events():
    for event in EVENTS:
        new_event = Event(
            image = event['image'],
            title = event['title'],
            description = event['description'],
            location = event['location'],
            event_date = event['event_date']
        )
        db.session.add(new_event) 
    db.session.commit()
    print("Events added!")

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        seed_events()
