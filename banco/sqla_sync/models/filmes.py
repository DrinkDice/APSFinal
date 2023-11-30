import uuid
import sqlalchemy as sa
from sqlalchemy import Column, String, DateTime, Float, CheckConstraint
from sqlalchemy import LargeBinary
from sqlalchemy.sql import func
from models.model_base import ModelBase

class Filme(ModelBase):
    __tablename__ = 'filmes'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    movie = Column(String(45), unique=True, nullable=False)
    released_year = Column(DateTime, default=func.now(), server_default=None, index=True)
    rating = Column(Float, CheckConstraint('rating >= 1.0 AND rating <= 10.0'), nullable=False)
    director = Column(String(45), nullable=False)

    def __repr__(self):
        return f'<Filme: {self.movie}>'
    


