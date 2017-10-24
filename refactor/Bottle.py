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
        self['notes'] = []

    def convert(self, bottleDict):
        for i in bottleDict:
            self[i] = bottleDict[i]

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
        if self['price'] > 0:
            print("Price: " + str(self['price']))
        if len(self['notes']) > 0:
            for i in self['notes']:
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
        print("1: Quantity")
        print("2: Review")
        print("3: Price")
        print("4: Notes")
        print("5: Scheduled Opening")
        print("Or press enter to exit")
        choice = str.lower(input())
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
        elif choice == 'price' or choice == '3':
            print("Current price is " + str(self['price']))
            print("What did the bottle cost?")
            self['price'] = int(input())
        elif choice == 'notes' or choice == '4':
            print("Enter a note about the wine!")
            note = input()
            self['notes'].append(note)
        elif choice == 'schedule' or choice == '5':
            print("Is this wine drinkable at any time? [Y/N]")
            choice = input()
            if choice == 'Y' or choice == 'y':
                self['tags'].append("drinkable")
            else:
                print("What occasion are you saving this bottle for?")
                occasion = str.lower(input())
                if 'drinkable' in self['tags']:
                    self['tags'].remove('drinkable')
                self['tags'].append(occasion)
        else:
            return None

if __name__ == '__main__':

    a = Bottle("ancien 2012 shea vineyard pinot noir")
    b = Bottle("ancien pinot noir shea vineyard 2012")

    if a == b:
        print("the same")
    else:
        print("not the same")
