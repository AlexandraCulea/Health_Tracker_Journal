from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Activitati(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, unique = True)
    ore_dormite = db.Column(db.String(50))
    durata_activitati = db.Column(db.String(50))
    mic_dejun = db.Column(db.String(50))
    pranz = db.Column(db.String(50))
    cina = db.Column(db.String(50))

class Simptome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, unique = True)
    simptom_input = db.Column(db.String(255))
    simptom_select = db.Column(db.String(255))


class StareDeSpirit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, unique = True)
    stare = db.Column(db.String(50))
    emotie = db.Column(db.String(50))

class Obiectiv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ore_dormite = db.Column(db.String(50))
    durata_activitati = db.Column(db.String(50))


