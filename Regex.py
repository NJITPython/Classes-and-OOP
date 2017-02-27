# RE - Regular Expressions
import re
pattern = re.compile(r'\d\d\d')
#if re.search(pattern, line): print(line)

def main():
    fh = open('raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line):  # searches for Lenore or Nevermore
            print(line, end='')

if __name__ == "__main__": main()
'''
    fh = open('raven.txt')
    for line in fh:
       match = re.search('(Len|Neverm)ore', line)
       if match:
           print(match.group())

    fh = open('raven.txt')
    for line in fh:
       print(re.sub('(Len|Neverm)ore', '###', line), end = '')  #sub is search and replace
 
    fh = open('raven.txt')
    for line in fh:
       match = re.search('(Len|Neverm)ore', line)
       if match:
           print(line.replace(match.group(), '###'), end = '')
#adding some efficiency  / pattern does not need to be compiled over and over again
    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
       if re.search(pattern, line):
           print(line, end='')

    
'''
