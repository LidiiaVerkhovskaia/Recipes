from app import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(120))
    ingredients = db.Column(db.String(256))
    steps = db.Column(db.String(512))
    time = db.Column(db.String(64))

