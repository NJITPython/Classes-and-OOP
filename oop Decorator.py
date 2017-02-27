'''
decorators are special functions which return other functions
the function 'color' turns into accessor because we are using decorator function
decorator change behavior of an object 
'''
class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    @property   #decorator
    def color(self):   
        return self.propertites.get('color', None)
    
    @color.setter(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['color']

    
    

def main():
    #donald = Duck(color = 'blue')
    donald = Duck()
    donald.color = 'blue'
    #print(donald.get_property('color'))
    print(donald.color)

if __name__ == "__main__": main()
