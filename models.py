from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_image = "data:image/png;base64,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"

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    '''Pet Model'''
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        return self.photo_url or default_image