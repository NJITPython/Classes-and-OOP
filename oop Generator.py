'''
generators
range is not inclusive, it goes up to last element.  Range function has 3
arguments: (start, stop, step)
__init__ - defines constructor
__iter__ - makes an object an iterable object
yield makes it generator
generator generates iterable object
when the object is used in content of iterable - for example in "for" loop, iterable
  method is called automatically
'''

class inclusive_range:
    def __init__(self, * args):
        numargs = len(args)
        # displays a message to the user if there is no argument
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i   # yield makes it generator  
            i += self.step
def main():
    #o = range(25)
    o = inclusive_range(5, 25,5)
    for i in o: print(i, end = ' ')
    #  for i in inclusive_range(25): print(i, end = ' ')  #alt way

if __name__ == "__main__": main()


'''
class inclusive_range:
    def __init__(self): pass   #constructor

    def __iter__(self): pass   #iterator
def main():
    o = range(25)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()
'''
