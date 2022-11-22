from ..database.db import db

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    frontImg = db.Column(db.String(200))
    move1 = db.Column(db.String(20))