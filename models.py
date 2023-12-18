from app import db

class CachedResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(255), unique=True, nullable=False)
    data = db.Column(db.JSON, nullable=False)