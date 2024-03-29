"""
Form Mr-Majr-k
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/words.db"

db = SQLAlchemy(app)


class Word(db.Model):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word = Column(String(5), unique=True, nullable=False)
    letter_1 = Column(String(1), nullable=False)
    letter_2 = Column(String(1), nullable=False)
    letter_3 = Column(String(1), nullable=False)
    letter_4 = Column(String(1), nullable=False)
    letter_5 = Column(String(1), nullable=False)

    def __init__(self, word: str, letter_1: str, letter_2: str, letter_3: str,
                 letter_4: str, letter_5: str) -> None:
        self.word = word
        self.letter_1 = letter_1
        self.letter_2 = letter_2
        self.letter_3 = letter_3
        self.letter_4 = letter_4
        self.letter_5 = letter_5


def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
