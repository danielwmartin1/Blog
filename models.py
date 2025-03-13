from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import pytz

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f'<Post {self.title}>'

    @property
    def formatted_created_at(self):
        return self.created_at.astimezone(pytz.timezone('America/New_York')).strftime('%Y-%m-%d %H:%M:%S %Z')

    @property
    def formatted_updated_at(self):
        return self.updated_at.astimezone(pytz.timezone('America/New_York')).strftime('%Y-%m-%d %H:%M:%S %Z')
