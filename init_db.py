from pokemon import db
from pokemon.models.pokemon import Pokemon
from pokemon import app

#clear it out
with app.app_context():
    db.drop_all()
#set it back up
    db.create_all()