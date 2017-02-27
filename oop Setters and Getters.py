# oop Setters and Getters - using accessor methods
'''
 abstraction
 polymorphism
 encapsulation
 inheritance
'''
# encapsulation - gives you control / allows to know how the data is being used

#!/usr/bin/python3

class Duck:
    '''
    def __init__(self, color = 'white'):
        self._color = color   #_color - underscore 1. attribute is used locally
                             # all access is going to be by methods within an object
    '''
# for the cases of multiple arguments use kwargs - which is dictionary
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', 'white')
        # to scale well, store all data properties in the dictionary
        #self.variables = kwargs
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    #for self.variables = kwargs, my accessors methods will change a bit
    '''
    def set_color(self, color):
        self.variables[color] = 'blue'

    def get_color(self):
        return self.variables.get('color', None)
    # or alternatively, we can generalize accessors methods
    def set_variables(self, k, v):
        self.variables[k] = v

    def get_variables(self, k):
        return self.variables.get(k, None)
    '''
def main():
    #donald = Duck()
    donald = Duck(color = 'blue')
    # alternative way # donald.set_color('blue')
    # another way if using dictionary then  - allows flexibility - for small amount
    # of code - to do different things ie. storing your object data in dictionary objects
    #donald = Duck(feet = 2)
    #donald.set_variable('color' = 'blue')
    #print(donald.get_variable('feet'))
    #print(donald.get_variable('color'))
    print(donald.get_color())
  #  donald.quack()
  #  donald.walk()

if __name__ == "__main__": main()
