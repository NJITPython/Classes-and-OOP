# classes / oop
'''
'''
# self is a reference to instantiated object i.e. when method is called 
# __init__ - is constructor

# simple fibonacci series
# the sum of two elements defines the next set
class Fibonacci():
    def __init__(self, a, b):
        print('constructor Init')
        self.a = a     # self.a - attach to an object (not class)
        self.b = b
        print('Out of constructor')

    def series(self):
        while(True):            
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b
            





print('Before Constructor')
f = Fibonacci(0,101)
print('After Constructor')

for r in f.series():
    if r > 100: break    
    print('****',r, end=' ')
