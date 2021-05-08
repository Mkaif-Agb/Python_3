def gensquares(n):
    for i in range(n):
      yield i**2

for i in gensquares(10):
    print(i)


import random

random.randint(1,10)
def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

for numb in rand_num(1,10,12):
    print(numb)


s = 'hello'
s = iter(s)
print(next(s))


