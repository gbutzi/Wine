from Bottle import *

vineyard = "Ancien"
grape = "Pinot Noir"
vintage = 2012
date_purchased = 2013
cost = 40
quantity = 1
comments = ""
date_consumed = ""

bottle = Bottle.create(vineyard=vineyard, grape=grape, vintage=vintage,
            date_purchased=date_purchased, cost=cost,
            quantity=quantity, comments=comments,
            date_consumed=date_consumed)
bottle.save()
