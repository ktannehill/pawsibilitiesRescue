#!/usr/bin/env python3

# Standard/ remote library imports
from random import choice as rc
import random
from datetime import datetime, timedelta
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
        'image': "https://images.unsplash.com/photo-1629957655360-5eeccf5253a6?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'title': "Paws in the Park Cleanup",
        'description': "Join us for a community park cleanup to create a safe and enjoyable space for our furry friends. We'll be clearing trails, picking up trash, and ensuring a clean environment for pets and their owners.",
        'location': "City Park, Denver",
        'event_date': "2024-03-10 09:00",
    },
    {
        'image': "https://images.unsplash.com/photo-1686345887586-c06b27bc21da?q=80&w=1925&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'title': "Adoption Day Extravaganza",
        'description': "Help us set up and organize our biggest adoption event of the year! Assist with booth setup, guide potential adopters, and create a welcoming atmosphere for our rescue animals.",
        'location': "Paw-sibilities Rescue Center",
        'event_date': "2024-04-15 11:00",
    },
    {
        'image': "https://images.unsplash.com/photo-1648632334867-f96cd2733eb5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'title': "Feline Friends Socialization Hour",
        'description': "Spend quality time with our adorable cats awaiting adoption. Engage in playtime, offer companionship, and help socialize our feline friends to improve their chances of finding forever homes.",
        'location': "Kitty Cuddle Haven, Denver",
        'event_date': "2024-05-05 03:00",
    },
    {
        'image': "https://images.unsplash.com/photo-1600044531557-f7902b86aace?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'title': "Dog Walking Adventure Group",
        'description': "Grab a leash and join us for a scenic dog walking adventure in the beautiful local trails. It's a great opportunity to exercise, enjoy nature, and provide our rescue dogs with much-needed outdoor time.",
        'location': "Local Trails, Denver",
        'event_date': "2024-06-20 10:00",
    },
    {
        'image': "https://images.unsplash.com/photo-1545249390-6bdfa286032f?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'title': "Pet Picture Day",
        'description': "Join us for a fun-filled day of capturing special moments with your beloved pets! Bring your furry friends to the local park, and our professional photographers will be on hand to take beautiful pictures. Cherish the memories forever!",
        'location': "Washington Park, Denver",
        'event_date': "2024-03-18 02:00",
    },
    {
        'image': "https://images.unsplash.com/photo-1683145634801-1eef1d43f663?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'title': "Senior Dogs Pup Cups",
        'description': "Treat your senior dogs to a delightful outing! We'll be taking our senior furry friends to Starbucks, where they can enjoy pup cups and receive lots of love. It's a heartwarming experience for both the dogs and their human companions!",
        'location': "Starbucks on ",
        'event_date': "2024-05-23 04:00",
    },
    {
        'image': "https://images.unsplash.com/photo-1620021030164-b0e70f5a5500?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'title': "Pet Adoption Fair",
        'description': "Join us for a heartwarming Pet Adoption Fair! We'll have adorable pets looking for their forever homes. Volunteers are needed to help with various tasks, including assisting visitors, answering questions, and ensuring a smooth adoption process. Make a difference in the lives of these animals and help them find loving families!",
        'location': "Local Community Center",
        'event_date': "2024-01-15 12:00",
    },
]

PETS = [
    "https://images.unsplash.com/photo-1472053217156-31b42df2319c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1522526469673-5b73aed892ff?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1587203915986-228a25ea2b7e?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1574144611937-0df059b5ef3e?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1544175089-f2e93cb8b8c5?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1594005374167-5fd900fb82c9?q=80&w=2037&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1622273509376-2d42c282dced?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1664481309598-eed92f7d2c60?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1610112645245-36020fc0e128?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1610620299042-4a7880ccb5b6?q=80&w=1776&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1622273509371-3ee5d873dcf6?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1593620659530-7f98c53de278?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1491485880348-85d48a9e5312?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1529906920574-628dc1e49f5a?q=80&w=2067&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1687632922201-164b5f753635?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1622273460358-08d791d3fccb?q=80&w=1893&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1597350406440-42b52c3f8746?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1610128977117-0d18144ae179?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1596751996853-b6ebb0808ba0?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1573865526739-10659fec78a5?q=80&w=1915&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
]

BREEDS = ["Domestic shorthair", "Domestic longhair", "Siamese", "Labrador", "Boxer", "Chihuahua", "Shepherd", "Poodle"]

def seed_events():
    for event in EVENTS:
        new_event = Event(
            image = event['image'],
            title = event['title'],
            description = event['description'],
            location = event['location'],
            event_date = datetime.strptime(str(event['event_date']), '%Y-%m-%d %H:%M')
        )
        db.session.add(new_event) 
    db.session.commit()
    print("Events added!")

def seed_users():
    for _ in range(50):
        fake_username = fake.email().split("@")[0]

        new_user = User(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            username = fake_username,
            email = fake.email(),
        )
        new_user.password_hash = "password"
        db.session.add(new_user)
    db.session.commit()
    print("Users added!")

def seed_pets():
    today = datetime.today()
    start_date = today - timedelta(days=365 * 8)
    end_date = today - timedelta(days=30 * 3)

    for img in PETS:
        new_pet = Pet(
            image = img,
            name = fake.first_name(),
            species = rc(["cat", "dog"]),
            breed = rc(BREEDS),
            est_birthday = fake.date_between(start_date=start_date, end_date=end_date),
            description = fake.paragraph(nb_sentences=7),
        )
        db.session.add(new_pet)
    db.session.commit()
    print("Pets added!")

def associate_user_events():
    for _ in range(30):
        user_instance = db.session.query(User).filter_by(id=random.randrange(1, 50)).first()
        event_instance = db.session.query(Event).filter_by(id=random.randrange(1, len(EVENTS))).first()

        existing_association = db.session.query(UserEvent).filter_by(
            user_id=user_instance.id, event_id=event_instance.id).first()

        if not existing_association:
            new_user_event = UserEvent(user_id=user_instance.id, event_id=event_instance.id)
            db.session.add(new_user_event)
    db.session.commit()
    print("Associations added!")

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        clear_tables()
        seed_events()
        seed_users()
        seed_pets()
        associate_user_events()
