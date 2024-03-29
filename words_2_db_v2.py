from flask import Flask
from models.word import db, Word, create_tables
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/words.db"

words_list = ["Stern", "Stand", "Stamm", "Stein", "Staub", "Sturm", "Stadt",
              "Stufe", "Stiel", "Blatt", "Blüte", "Block", "Blase", "Blick",
              "Blech", "Blend", "Blitz", "Bleib", "Rasch", "Hasse"]


def words_2_db(words: list[str]) -> None:
    for word in words:
        word = word.upper()
        word_list = list(word)
        letter_1 = word_list[0]
        letter_2 = word_list[1]
        letter_3 = word_list[2]
        letter_4 = word_list[3]
        letter_5 = word_list[4]

        try:
            new_word = Word(word, letter_1, letter_2, letter_3, letter_4,
                            letter_5)
            db.session.add(new_word)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(f"Das Wort '{word}' existiert bereits in der Datenbank.")


if __name__ == '__main__':
    with app.app_context():
        create_tables()
        db.init_app(app)
        words_2_db(words_list)
