from peewee import SqliteDatabase, Model, TextField, BooleanField, ForeignKeyField
db = SqliteDatabase('db.db')

class Table(Model):


        class Meta:
            database =db

class Category(Table):
    name =TextField()

class Auth(Table):
    name = TextField()

class Info(Table):
    API = TextField()
    Description = TextField()
    Auth =  ForeignKeyField(Auth, null=True)
    HTTPS = BooleanField()
    Cors = BooleanField(null=True)
    Link = TextField()
    Category = ForeignKeyField(Category)
    

db.connect()
db.create_tables(
    [Category, Info, Auth], safe=True)
db.close()