import math
import trie.py
def foo(num):
    for i in range(30,-1,-2):
        ander = int(math.pow(2,i)+math.pow(2,i+1))
        yield (ander & num) >> i

def genArray(i, mask):
    a = foo(i)
    b = []
    h = int((mask / 2))
    for k in a:
        b.append(k)
    if mask % 2:
       
        b = b[0:h+1]
        b[h] = b[h] & 3
        for k in b:
            print('{:02b}'.format(k))
        #create
        b[h] = b[h] + 1
        for k in b:
            print('{:02b}'.format(k))
        #create again
    else:
        print("even")
        b = b[:h]
        for k in b:
            print('{:02b}'.format(k))
genArray(16777216,16)        
