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
        'event_date': "2024-05-05 15:00",
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
        'event_date': "2024-03-18 14:00",
    },
    {
        'image': "https://images.unsplash.com/photo-1683145634801-1eef1d43f663?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'title': "Senior Dogs Pup Cups",
        'description': "Treat your senior dogs to a delightful outing! We'll be taking our senior furry friends to Starbucks, where they can enjoy pup cups and receive lots of love. It's a heartwarming experience for both the dogs and their human companions!",
        'location': "Starbucks on Alameda",
        'event_date': "2024-05-23 16:00",
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
    {
        'image': "https://images.unsplash.com/photo-1574144611937-0df059b5ef3e?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "An active and playful tabby cat seeking a home with room for exploration and interactive play. Ideal for families who enjoy an energetic feline companion."
    },
    {
        'image': "https://images.unsplash.com/photo-1597350406440-42b52c3f8746?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A gentle and affectionate dog with a graceful disposition, perfect for those who appreciate quiet evenings and cozy companionship."
    },
    {
        'image': "https://images.unsplash.com/photo-1610128977117-0d18144ae179?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A mysterious black cat who loves to explore and investigate. If you enjoy the enigmatic charm of feline curiosity, this one's for you."
    },
    {
        'image': "https://images.unsplash.com/photo-1664481309598-eed92f7d2c60?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A sociable and friendly dog, always ready for long walks and outdoor adventures. Best suited for active individuals or families who love an energetic canine friend."
    },
    {
        'image': "https://images.unsplash.com/photo-1472053217156-31b42df2319c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A shy yet sweet cat looking for a patient and understanding home. With a little time and love, this feline friend will become a devoted and loyal companion."
    },
    {
        'image': "https://images.unsplash.com/photo-1594005374167-5fd900fb82c9?q=80&w=2037&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A laid-back dog that enjoys the leisurely side of life. Perfect for those seeking a low-energy, easygoing canine companion for cozy moments at home."
    },
    {
        'image': "https://images.unsplash.com/photo-1687632922201-164b5f753635?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A senior dog with a heart full of love and a gentle spirit. Despite age, this canine friend is affectionate and ready to bring warmth to your home."
    },
    {
        'image': "https://images.unsplash.com/photo-1610620299042-4a7880ccb5b6?q=80&w=1776&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A social cat that thrives on meeting new people. With a friendly demeanor and playful attitude, this feline is perfect for households that enjoy social interaction."
    },
    {
        'image': "https://images.unsplash.com/photo-1529906920574-628dc1e49f5a?q=80&w=2067&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A goofy and lovable dog with a talent for humor. If you're looking for a companion that can bring laughter and joy to your home, this one's a perfect match."
    },
    {
        'image': "https://images.unsplash.com/photo-1491485880348-85d48a9e5312?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A unique and resilient cat with special needs, but a heart full of love to share. Ideal for those ready to provide a caring and understanding home for this extraordinary feline."
    },
    {
        'image': "https://images.unsplash.com/photo-1593620659530-7f98c53de278?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A spirited boxer pup with an enthusiasm for life and boundless energy. Ideal for families or individuals seeking a playful and joyful companion for adventures and everyday moments."
    },
    {
        'image': "https://images.unsplash.com/photo-1622273509371-3ee5d873dcf6?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A mellow ragdoll cat that excels in relaxation. This feline friend is perfect for homes that appreciate the art of unwinding, providing a serene presence for tranquil moments."
    },
    {
        'image': "https://images.unsplash.com/photo-1610112645245-36020fc0e128?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A courageous dachshund mix with a heart full of bravery. This canine companion is ready to face the world with you, making it an ideal match for those seeking a loyal and resilient friend."
    },
    {
        'image': "https://images.unsplash.com/photo-1622273509376-2d42c282dced?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A cuddly orange tabby cat with a penchant for affectionate moments. This charming feline friend is an excellent choice for anyone seeking a warm and loving companion for quiet evenings and cozy naps."
    },
    {
        'image': "https://images.unsplash.com/photo-1544175089-f2e93cb8b8c5?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "An energetic border collie with a love for mental challenges and outdoor activities. Perfect for individuals or families with an active lifestyle, this canine companion thrives on stimulation and engagement."
    },
    {
        'image': "https://images.unsplash.com/photo-1622273460358-08d791d3fccb?q=80&w=1893&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A reserved Siamese cat seeking a calm and patient home. With a sweet and gentle disposition, this feline friend is an ideal match for those who appreciate the quieter moments of companionship."
    },
    {
        'image': "https://images.unsplash.com/photo-1596751996853-b6ebb0808ba0?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A devoted Labrador ready to become your loyal and affectionate friend. Known for their friendly nature, this canine companion is well-suited for families looking for an all-around loving and gentle pet."
    },
    {
        'image': "https://images.unsplash.com/photo-1522526469673-5b73aed892ff?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A curious tuxedo cat with a penchant for exploration and discovery. This feline friend is an excellent match for homes that appreciate the inquisitive nature of a charming and sophisticated companion."
    },
    {
        'image': "https://images.unsplash.com/photo-1587203915986-228a25ea2b7e?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "An easygoing terrier mix, perfect for a laid-back lifestyle. This lovable canine companion enjoys leisurely walks and relaxed moments, making it an excellent fit for those who cherish a calm atmosphere."
    },
    {
        'image': "https://images.unsplash.com/photo-1573865526739-10659fec78a5?q=80&w=1915&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        'description': "A lively calico cat with an affinity for playtime and interactive toys. Ideal for families or individuals seeking a feline friend to brighten their days with endless energy and charm."
    }
]

BREEDS = ["Domestic shorthair", "Domestic longhair", "Siamese", "Labrador", "Boxer", "Chihuahua", "Shepherd", "Poodle"]

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

def seed_admins():
    new_user = User(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        username = "admin",
        email = "admin@email.com",
    )
    new_user.admin = True
    new_user.password_hash = "password"
    db.session.add(new_user)
    for _ in range(4):
        fake_username = fake.email().split("@")[0]

        if len(fake_username) < 5:
            fake_username + "xyz"

        new_user = User(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            username = fake_username,
            email = fake.email(),
        )
        new_user.admin = True
        new_user.password_hash = "password"
        db.session.add(new_user)
    db.session.commit()
    print("Admins added!")

def seed_users():
    for _ in range(25):
        fake_username = fake.email().split("@")[0]

        if len(fake_username) < 5:
            fake_username + "789"

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

    for pet in PETS:
        new_pet = Pet(
            image = pet["image"],
            name = fake.first_name(),
            species = rc(["cat", "dog"]),
            breed = rc(BREEDS),
            sex = rc(["female", "male"]),
            est_birthday = fake.date_between(start_date=start_date, end_date=end_date),
            description = pet["description"],
        )
        db.session.add(new_pet)
    db.session.commit()
    print("Pets added!")

def associate_user_events():
    for _ in range(30):
        user_instance = db.session.query(User).filter_by(id=random.randrange(1, 30)).first()
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
        seed_admins()
        seed_users()
        seed_pets()
        associate_user_events()
