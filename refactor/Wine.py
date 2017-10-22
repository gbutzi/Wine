#!/usr/bin/python3
import Rack
import Bottle
import json
import pdb
import sys

class Wine:

    path = '.wine.db'
    affirm = ['y', 'yes', 'continue', 'YES', 'Yes', 'Y']

    # Wine.py is meant to be a driver for Rack and Bottle

    def __init__(self):
        pass

    def load(self):
        with open(self.path, 'r') as f:
            rackList = json.load(f)
            rack = Rack.Rack()
            rack.convert(rackList)
            return rack

    def write(self, rack):
        with open(self.path, 'w') as f:
            json.dump(rack.Rack, f)

    def destroy(self):
        c = Rack.Rack()
        self.write(c)

    def add(self, taglist):
        rack = self.load()
        newBottle = Bottle.Bottle(taglist)
        rack.add(newBottle)
        self.write(rack)

    def drink(self, taglist):
        rack = self.load()
        bottle = rack.select(taglist)
        if bottle is not None:
            bottle.drink()
            self.write(rack)
        else:
            print("That bottle isn't in the rack")

    def list(self):
        rack = self.load()
        rack.printRack()
    
    def delete(self, taglist):
        rack = self.load()
        rack.delete(taglist)
        self.write(rack)

    def look(self, taglist):
        rack = self.load()
        selectedBottle = rack.select(taglist)
        if selectedBottle is not None:
            selectedBottle.view()
        else:
            print("That bottle isn't in the rack")
    
    def edit(self, taglist):
        rack = self.load()
        selectedBottle = rack.select(taglist)
        if selectedBottle is None:
            print("That bottle isn't in the rack")
            return None
        while 1:
            selectedBottle.edit()
            print("Continue editing? [Y/N}")
            choice = input()
            if choice not in self.affirm:
                break
        self.write(rack)

if __name__ == '__main__':
    '''
    wine = Wine()
    wine.destroy()
    wine.add("a sample bottle")
    wine.drink("bottle")
    wine.edit("sample")
    wine.look("a")
    wine.add("a sample bottle")
    wine.add("a different bottle")
    wine.delete("bottle")
    wine.drink("not here")
    wine.edit("not here")
    wine.delete("not here")
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
    elif sys.argv[1] == 'look' or sys.argv[1] == 'list':
        if len(sys.argv) == 2:
            Wine().list()
        else:
            Wine().look(taglist)
    elif sys.argv[1] == 'delete':
        Wine().delete(taglist)
    elif sys.argv[1] == 'destroy':
        print("This will destroy the database. Are you sure? [Y/N]")
        choice = input()
        if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
            Wine().destroy()
    elif sys.argv[1] == 'edit' or sys.argv[1] == 'select':
        Wine().edit(taglist)
    else:
        help()
