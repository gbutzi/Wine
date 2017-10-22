import Bottle
import pdb

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
