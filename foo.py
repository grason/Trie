import math
def foo(num):
    for i in range(30,-1,-2):
        ander = int(math.pow(2,i)+math.pow(2,i+1))
        yield (ander & num) >> i
z = 0
print('{:032b}'.format(2289985753))
for k in foo(2289985753):
    print(k)
