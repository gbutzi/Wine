import pdb

class test:

    def __init__(self):
        string = "this is a string"
        quantity = 2

    def __getattribute__(self, name):
        if name == 'string':
            return self.string
        elif name == 'quantity':
            return self.quantity
        return name

    def __getitem__(self, item):
        return item

