from pokemon import db
from pokemon.models.pokemon import Pokemon
from flask import Flask

# Clear it all out
def create_app():
    app = Flask(__name__)

    with app.app_context():
        db.drop_all()
        # Set it back up
        db.create_all()

    return app
