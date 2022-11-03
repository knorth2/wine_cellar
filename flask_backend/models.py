from peewee import *
import datetime

DATABASE = SqliteDatabase('wine.sqlite')

class Wine(Model):
    name = CharField()
    img = CharField()
    vintage = CharField()
    region = CharField()
    rating = CharField()
    price = CharField()
    quantity = CharField()
    notes = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Wine], safe=True)
    print("TABLES Created")
    DATABASE.close()