import hashlib
import pdb
from json import JSONEncoder

class Bottle(JSONEncoder):

    #{"quantity": int, "index": int, "name": "a string", "review" = ["a list", "of strings"]}

    stats = {}

    def __init__(self, tagstring):
        self.stats['index'] = 0
        self.stats['tags'] = []
        self.stats['quantity'] = 1
        self.stats['review'] = []
        lowtags = tagstring.lower()
        listing = lowtags.split()
        for i in listing:
            self.stats['tags'].append(i)
        self.stats['name'] = tagstring
        self.stats['price'] = 0

        '''
        self.index = 0
        self.tags = []
        self.quantity = 0
        self.review = []
        lowtags = tagstring.lower()
        listing = lowtags.split()
        for i in listing:
            self.tags.append(i)
        self.tags.sort()
        self.name = tagstring
        self.quantity += 1
        self.index = 0
        self.price = 0
        '''

    def default(self):
        return stats

    def from_json(json_object):
        bottle = Bottle("")
        for i in json_object:
            bottle[i] = json_object[i]
        
        return bottle

    def drink(self):
        self.stats['quantity'] -= 1
        print("What do you think?")
        thoughts = input()
        print("What is the date?")
        date = input()
        r = date + ": " + thoughts
        self.stats['review'].append(r)

    def setIndex(self, i):
        self.stats['index'] = i

    def printTags(self):
        for i in self.stats['tags']:
            print(i)

    def view(self):
        print(self.stats['name'])
        print("In Stock: " + str(self.stats['quantity']))
        for i in self.stats['review']:
            print(i)

    def __eq__(self, bottle):
        if not isinstance(bottle, Bottle): return False
        selftags = ' '.join(sorted(self.stats['tags']))
        cmptags = ' '.join(sorted(bottle.stats['tags']))

        sHasher = hashlib.sha256()
        cHasher = hashlib.sha256()

        sHasher.update(selftags.encode())
        cHasher.update(cmptags.encode())

        sHash = sHasher.hexdigest()
        cHash = cHasher.hexdigest()

        return sHash == cHash

    def __hash__(self):
        return id(self)

    def edit(self):
        print("What would you like to edit?")
        print("1: quantity")
        print("2: review")
        print("Or press enter to exit")
        choice = input()
        if len(choice) == 0:
            return None
        elif choice == 'quantity' or '1':
            print("Change quantity to what?")
            self.stats['quantity'] = int(input())
            print("Quantity is now " + str(self.stats['quantity']))
        elif choice == 'review' or '2':
            print("What do you think?")
            thoughts = input()
            print("What is the date?")
            date = input()
            r = date + ": " + thoughts
            self.stats['review'].append(r)
        else:
            return None

if __name__ == '__main__':

    a = Bottle("ancien 2012 shea vineyard pinot noir")
    b = Bottle("ancien pinot noir shea vineyard 2012")

    if a == b:
        print("the same")
    else:
        print("not the same")
