import hashlib
import pdb

class Bottle(dict):

    #{"quantity": int, "index": int, "name": "a string", "review" = ["a list", "of strings"]}

    def __init__(self, tagstring):
        self['index'] = 0
        self['tags'] = []
        self['quantity'] = 0
        self['review'] = []
        lowtags = tagstring.lower()
        listing = lowtags.split()
        for i in listing:
            self['tags'].append(i)
        self['tags'].sort()
        self['name'] = tagstring
        self['quantity'] += 1
        self['index']= 0
        self['price'] = 0

    def drink(self):
        self['quantity'] -= 1
        print("What do you think?")
        thoughts = input()
        print("What is the date?")
        date = input()
        r = date + ": " + thoughts
        self['review'].append(r)

    def setIndex(self, i):
        self['index'] = i

    def printTags(self):
        for i in self['tags']:
            print(i)

    def view(self):
        print(self['name'])
        print("In Stock: " + str(self['quantity']))
        for i in self['review']:
            print(i)

    def __eq__(self, bottle):
        if not isinstance(bottle, Bottle): return False
        selftags = ' '.join(sorted(self['tags']))
        cmptags = ' '.join(sorted(bottle['tags']))

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
        elif choice == 'quantity' or choice == '1':
            print("Change quantity to what?")
            self['quantity'] = int(input())
            print("Quantity is now " + str(self['quantity']))
        elif choice == 'review' or choice == '2':
            print("What do you think?")
            thoughts = input()
            print("What is the date?")
            date = input()
            r = date + ": " + thoughts
            self['review'].append(r)
        else:
            return None

if __name__ == '__main__':

    a = Bottle("ancien 2012 shea vineyard pinot noir")
    b = Bottle("ancien pinot noir shea vineyard 2012")

    if a == b:
        print("the same")
    else:
        print("not the same")
