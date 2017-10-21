#!/usr/bin/python3 
import Rack
#import Bottle
import json 
import pdb
import sys

class Wine:

    path = '/home/greg/Wine/wine.db'
    affirm = ['y', 'yes', 'continue', 'YES', 'Yes', 'Y']


    # Wine.py is meant to be a driver for Rack and Bottle.

    def __init__(self):
        pass

    def add(self, taglist):
        # create a bottle from the taglist. Add the bottle to the rack.
        # if a bottle or bottles fits the taglist given, display
        # the list and prompt me to select a bottle.

        rack = Rack.Rack()
        newBottle = rack.makeBottle(taglist)

        rack.addBottle(newBottle)
        
    def drink(self, taglist):
        rack = Rack.Rack()
        openBottle = rack.select(taglist)
        rack.drink(openBottle)
        rack.setIndices(rack.rack)
        json.dump(self.rack, open(self.path, 'w'))


    def list(self):
        rack = Rack.Rack()
        rack.printRack()

    def delete(self, taglist):
        rack = Rack.Rack()
        rack.delete(taglist)

    def look(self, taglist):
        rack = Rack.Rack()
        selectedBottle = rack.select(taglist)
        rack.view(selectedBottle)

    def destroy(self):
        c = []
        with open(self.path, "w") as f:
            json.dump(c, open(self.path, 'w'))

    def edit(self, taglist):
        rack = Rack.Rack()
        selectedBottle = rack.select(taglist)
        while 1:
            rack.editBottle(selectedBottle)
            print("Continue editing? [Y/N}")
            choice = input()
            if choice not in self.affirm:
                break
        json.dump(rack.rack, open(self.path, 'w'))


if __name__ == '__main__':
    '''
    wine = Wine()
    wine.add("ancien 2012 pinot noir")
    wine.add("ancien chardonnay 2013")
    wine.add("ancien pinot noir 2012")

    #pdb.set_trace()
    wine.list()

    wine.drink("ancien 2012 pinot noir")
    wine.look("ancien 2012 pinot noir")
    wine.delete("chardonnay")
    wine.list()
    '''

    def help():
        print("Usage: 'wine add list of tags' will add a wine with that taglist")
        print("'wine drink list of tags' will select the bottle listed and let you review it")
        print("'wine list' will list everything in the rack")
        print("'wine delete list of tags' will select the bottle listed and delete it")
        print("'wine look list of tags' will select the bottle listed and print its info")
        print("'wine edit list of tags' will select the bottle listed and let you edit it")
        print("'wine destroy' will delete the rack permanently. Don't do this.")


    taglist = ' '.join(sys.argv[2:])

    if len(sys.argv) <= 1:
        help()
    elif sys.argv[1] == 'add':
        Wine().add(taglist)
    elif sys.argv[1] == 'drink':
        Wine().drink(taglist)
    elif sys.argv[1] == 'list':
        Wine().list()
    elif sys.argv[1] == 'delete':
        Wine().delete(taglist)
    elif sys.argv[1] == 'look':
        if len(sys.argv) == 2:
            Wine().list()
        else:
            Wine().look(taglist)
    elif sys.argv[1] == 'destroy':
        print("This will destroy the database. Are you sure? [Y/N]")
        choice = input()
        if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
            Wine().destroy()
    elif sys.argv[1] == 'edit' or sys.argv[1] == 'select':
        Wine().edit(taglist)
    else:
        help()
