import json
import pdb
import Bottle

class Rack:

    rack = []

    path = ".wine.db"

    def __init__(self):
        pass

    def makeBottle(self, tagstring):

        bottle = {}
        bottle['tags'] = []
        bottle['quantity'] = 1
        bottle['review'] = []
        lowtags = tagstring.lower()
        listing = tagstring.split()
        for i in listing:
            bottle['tags'].append(i.capitalize())
        bottle['name'] = ' '.join(bottle['tags'])
        bottle['price'] = 0
        bottle['index'] = 0
        bottle['notes'] = []
        return bottle

    def drinkBottle(self, bottle):
        bottle['quantity'] -= 1
        print("What do you think?")
        thoughts = input()
        print("What is the date?")
        date = input()
        r = date + ": " + thoughts
        bottle['review'].append(r)

    def printTags(self, bottle):
        for i in bottle['tags']:
            print(i)

    def view(self, bottle):
        print(bottle['name'])
        if bottle['price'] > 0:
            print("Price: " + str(bottle['price']))
        print("In Stock: " +str(bottle['quantity']))
        for i in bottle['review']:
            print(i)
        if len(bottle['notes']) > 0:
            for i in bottle['notes']:
                print(i)

    def editBottle(self, bottle):
        print("What would you like to edit?")
        print("1: quantity")
        print("2: review")
        print("3: price")
        print("4: notes")
        print("or press enter to exit")
        choice = input()
        if len(choice) == 0:
            return None
        elif choice == 'quantity' or choice == '1':
            print("Change quantity to what?")
            bottle['quantity'] = int(input())
            print("Quantity is now " + str(bottle['quantity']))
        elif choice == 'review' or choice == '2':
            print("What do you think?")
            thoughts = input()
            print("What is the date?")
            date = input()
            r = date + ": " + thoughts
            bottle['review'].append(r)
        elif choice == 'price' or choice == '3':
            print("Enter the price")
            bottle['price'] = int(input())
        elif choice == 'notes' or choice == '4':
            print("Add notes:")
            bottle['notes'].append(input())
        else:
            return None

    def setIndices(self, rack):
        i = 0
        while i < len(rack):
            rack[i]['index'] = i
            i += 1

    def contains(self, bottle):
        self.rack = json.load(open(self.path, 'r'))
        if bottle in self.rack:
            return True
        else:
            return False

    def addBottle(self, bottle):
        try:
            self.rack = json.load(open(self.path, 'r'))
        except json.decoder.JSONDecodeError:
            self.rack = []

        flag = False
        for i in self.rack:
            if i == bottle:
                i['quantity'] += 1
                flag = True
                break
        if flag == False:
            self.rack.append(bottle)

        self.setIndices(self.rack)

        json.dump(self.rack, open(self.path, 'w'))

    def searchRack(self, tags):
        self.rack = json.load(open(self.path, 'r'))

        # for each word in the tags given, we create a set
        # we iterate through the rack and for each set,
        # we add a bottle if the taglist contains the tag.
        # after, we should be able to get the union of all the sets
        # and that's the list of bottles that matches our search.

        setlist = []
        taglist = tags.split()

        for word in taglist:
            s = set()
            for bottle in self.rack:
                if word in bottle['tags']:
                    s.add(bottle['index'])
            setlist.append(frozenset(s))

        results = frozenset.intersection(*setlist)
        return results
    
    def select(self, tags):
        wineset = tuple(self.searchRack(tags))
        self.rack = json.load(open(self.path, 'r'))

        if len(wineset) == 1:
            return self.rack[wineset[0]]
        
        for i in wineset:
            print(str(i) + ": " + self.rack[i]['name'])

        print("Type the index of the wine you want to select")

        selection = int(input())

        bottle = self.rack[i]
        return bottle

        print("Wine not found")
        return None

    def delete(self, tags):
        bottle = self.select(tags)
        if bottle is not None:
            self.rack = json.load(open(self.path, 'r'))
            self.rack.pop(bottle['index'])
            self.setIndices(self.rack)
            json.dump(self.rack, open(self.path, 'w'))
        else:
            print("Wine is not in the rack")

    def printRack(self):
        self.rack = json.load(open(self.path, 'r'))
        for i in self.rack:
            if i is not None:
                print(i['name'] + ", " + "quantity: " + str(i['quantity']))

if __name__ == '__main__':

    a = Rack().makeBottle('2012 ancien pinot noir')
    b = Rack().makeBottle('2013 ancien chardonnay')
    c = Rack().makeBottle('2012 pinot grigio')
    d = Rack().makeBottle('2014 ancien pinot noir')

    rack = Rack()
    rack.addBottle(a)
    rack.addBottle(b)
    rack.addBottle(c)
    rack.addBottle(d)


    #l = rack.searchRack('pinot noir')
    rack.printRack()
    #rack.select('pinot noir')
    rack.delete('pinot noir')
    #print("Deleting pinot noir")
    rack.printRack()

