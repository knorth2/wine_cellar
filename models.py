from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('wine.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

class Wine(Model):
    name = CharField()
    vintage = IntegerField()
    region = CharField()
    rating = CharField()
    price = IntegerField()
    quantity = IntegerField()
    notes = CharField()
    user = ForeignKeyField(User, backref='wine')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Wine], safe=True)
    print("TABLES Created")
    DATABASE.close()