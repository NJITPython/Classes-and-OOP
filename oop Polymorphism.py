'''
polymorphism - using of one object of one particular class as if it was another
object of another class
objects in the python, do not care what the name of the class is i.e
objects is loosely typed (i.e. duck typed)
'''
# The below is code that defines the Duck class 
class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('The duck cannot bark')

    def fur(self):
        print('The duck has fathers')

# The below is code that deines the Dog class 
class Dog:
    def bark(self):
        print('Woof!')

    def fur(self):
        print('The dog has brown and white fur')

    def walk(self):
        print('Walks like a dog')

    def quack(self):
        print('The dog cannot quack')
        
def main():
    donald = Duck()
    fido = Dog()
    in_the_forest(donald)
    in_the_pond(fido)
    '''
    for o in (donald, fido):
        o.quack()
        o.walk()
        o.bark()
        o.fur()'''

def in_the_forest(dog):
    dog.bark()
    dog.fur()
##def in_the_forest(cat):
##    cat.bark()
##    cat.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

if __name__ == "__main__": main()
