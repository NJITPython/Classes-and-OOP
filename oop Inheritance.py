'''
Inheritance - when one class inherits property from another class
Class inherited from is called Base class or Parent class 
  by puting in (parent class), class Duck inherits from class Animal
  in OOP, we will say Duck 'is' an animal
  walk method in Duck overrides walk method in Animal
  supur function allows to incorporate method from the parent class

Creating base class which contain common properties to classes which will inherit
from the base class and therefore, it does make code re-usable.
'''
class Animal:
    def talk(self): print('I have something to say')
    def walk(self): print('Hey! I am walking here')
    def clothes(self): print('I have nice clothes')

class Duck(Animal):  
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()
        print('Walks like a duck.')

class Dog(Animal):
    def clothes(self):
         print('I have brown and white fur')
         
def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()

    fido = Dog()
    fido.walk()
    fido.clothes()

if __name__ == "__main__": main()
