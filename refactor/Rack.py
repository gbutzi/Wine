import Bottle
import pdb
import random

class Rack():

    Rack = []
    
    def __init__(self):
        pass

    def convert(self, rackList):
        self.Rack = []
        for i in rackList:
            b = Bottle.Bottle('')
            b.convert(i)
            self.Rack.append(b)
    
    def add(self, bottle):
        flag = False
        for i in self.Rack:
            if i == bottle:
                i['quantity'] += 1
                flag = True
                break
        if flag == False:
            self.Rack.append(bottle)

    def next(self, *tags):

        # Okay, this function is a little ugly, so Imma explain some
        # stuff about what it's doing so that when I come back later
        # to clean it up, i'm not quite as lost as I will be otherwise.
        # The goal is to be able to say "wine next" and get a random
        # bottle that we're not saving for a special occasion, and also
        # be able to say "wine next pinot" or "wine next chardonnay" or
        # "wine next red" to get random, drinkable bottle of whatever is 
        # specified. This means that it needs to take a truly variable
        # length of arguments, which other functions haven't had to handle
        # yet; I deal with this by using *kargs, which means I have to pull
        # the string out of the tuple. That gets handled in the driver,
        # but I still have an empty string that sometimes gets passed in.
        # So that's part of it. 

        # I started out with a bottleList, and then I'd check the tags for a 
        # match and use list.remove() to pull non-matching bottles out. I ran
        # into a weird bug where sometimes I wasn't iterating over the full 
        # list; this is because python would pull out a bottle from the list,
        # the next bottle would get moved into that slot, and then the iterator
        # would end up skipping the (previously next) bottle. So instead, I use
        # a temp list, and if a bottle matches the tags, I add it to my
        # bottleList.

        # the bug can be reproed in python: 
        # l = [1,2,3,4,5,6]; for i in : if i > 3: l.remove(i)
        # l: [1,2,3,5]

        # There's still a small bug in this function: if I do "wine next pinot grigio"
        # it might return a pinot noir, and vice versa; gonna have to fix this one at
        # some point.

        tagstring = tags[0]
        tagList = tagstring.split(' ')
        bottleList = []
        for i in self.Rack:
            if "drinkable" in i['tags']:
                bottleList.append(i)

        if tagList[0] is not '':
            tempList = bottleList
            bottleList = []
            for t in tagList:
                for b in tempList:
                    if t in b['tags']:
                        bottleList.append(b)

        if len(bottleList) == 0:
            print("No bottles like that are drinkable right now")
            return None
        
        return random.choice(bottleList)

    def search(self, tags):

        setlist = []
        taglist = tags.split()

        for word in taglist:
            s = set()
            for bottle in self.Rack:
                if word in bottle['tags']:
                    s.add(bottle)
            setlist.append(frozenset(s))

        results = frozenset.intersection(*setlist)
        return results

    def select(self, tags):
        wineset = tuple(self.search(tags))

        if len(wineset) == 0:
            print("Wine not found")
            return None

        if len(wineset) == 1:
            return wineset[0]

        for i in wineset:
            print(str(self.Rack.index(i)) + ": " + i['name'])

        print("Type the index of the wine you want to select")

        selection = int(input())

        bottle = self.Rack[selection]
        return bottle

    def delete(self, tags):
        bottle = self.select(tags)
        if bottle is not None:
            self.Rack.remove(bottle)
        else:
            print("Wine is not in the rack")

    def printRack(self):
        for i in self.Rack:
            print(i['name'] + ", quantity: " + str(i['quantity']))

if __name__ == '__main__':

    a = Bottle.Bottle('2012 ancien pinot noir')
    b = Bottle.Bottle('2013 ancien chardonnay')
    c = Bottle.Bottle('2012 pinot grigio')
    d = Bottle.Bottle('2014 ancien pinot noir')

    rack = Rack()
    rack.add(a)
    rack.add(b)
    rack.add(c)
    rack.add(d)
    rack.add(a)
    rack.printRack()
    rack.delete('pinot noir')
    rack.printRack()
