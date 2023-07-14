from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('search_history.db')



class User(Model):
    name = CharField()
    telegram_id = IntegerField()
    search_history = CharField()

    class Meta:
        database = db