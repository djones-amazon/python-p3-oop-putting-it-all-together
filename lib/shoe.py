#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition=None):
        self.brand = brand
        self.size = size

    def get_size(self):
        print ('Retrieving shoe size')
        return self._size
    
    def set_size(self, size):
        if (type(size) == (int)):
            print (f'Setting size to {size}')
            self._size = size
        else:
            print ('size must be an integer')

    def cobble(self):
        self.condition = 'New'
        print ('Your shoe is as good as new!')
    
    size = property(get_size, set_size)