"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# example pets
pet1 = Pet(name='Scooby', species='Dog', age='4')
pet2 = Pet(name='Goldie', species='Dog', age='10')


db.session.add_all([pet1, pet2])

db.session.commit()



