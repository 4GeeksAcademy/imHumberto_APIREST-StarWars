from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    planet_weather: Mapped[str] = mapped_column(nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.planet_name,
            "weather": self.planet_weather,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = "characters"

    id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.character_name,
            "gender": self.gender,
            # do not serialize the password, its a security breach
        }