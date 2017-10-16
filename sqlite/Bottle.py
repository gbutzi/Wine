import peewee

database = peewee.SqliteDatabase(".wine.db")

class BaseModel(peewee.Model):
  class Meta:
    database = database

class Bottle(BaseModel):

	vineyard = peewee.CharField()
	region = peewee.CharField()
	grape = peewee.CharField()
	vintage = peewee.CharField()
	date_purchased = peewee.CharField()
	cost = peewee.IntegerField()
	quantity = peewee.IntegerField() 
	comments = peewee.CharField()
	date_consumed = peewee.CharField()

if __name__ == "__main__":
  try:
    Bottle.create_table()
  except peewee.OperationalError:
    print("Bottle Table already exists!")
