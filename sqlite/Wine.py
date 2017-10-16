from Bottle import *
import json

class Wine:

  def make(self):
      #Open the terms dictionary, then seek to the beginning of the file.
      #This makes sure that when we write the dictionary back to disk,
      #the old dictionary gets overwritten.
    archive = open('.terms.wne', 'r+')
    terms = {}

    terms = json.load(archive)
    archive.seek(0)

    vineyard = input('What vineyard? ')
    grape = input('What grape? ')
    region = input('What region? ')
    vintage = input('What year? ')
    date_purchased = int(input('When did you buy it? '))
    cost = int(input('How much was it? '))
    quantity = 1
    comments = ""
    date_consumed = ""

    bottle = Bottle.create(vineyard=vineyard, grape=grape, vintage=vintage,
                region = region, date_purchased=date_purchased, cost=cost,
                quantity=quantity, comments=comments,
                date_consumed=date_consumed)
    bottle.save()

    terms[vineyard] = 'vineyard'
    terms[grape] = 'grape'
    terms[region] = 'region'
      
    json.dump(terms, archive)
    archive.close()

  #I want to say "Wine list ancien pinot noir 2012" and have it return all the
  #ancien 2012 pinot noirs in the db.
  #
  #So I get a tuple of search words; i need to figure out what type of term each 
  #word is, construct the query, run the query to get a result, then print each result.

  def list(*args):
      archive = open('.terms.wne', 'r')
      terms = json.load(archive)
      archive.close()
      query_list = [] 

      for i in args:
          query_list.append(terms[i])
      
      print(query_list)

