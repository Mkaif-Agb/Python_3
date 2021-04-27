import datetime

t = datetime.time(5, 25, 41)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.min)
print(t.max)
print(t.resolution)

today = datetime.date.today()
print(today)

print(today.day)
print(datetime.date.max)
print(datetime.datetime.max)
print(datetime.date.min)


# REPLACE FUNCTIONALITY IN PYTHON#

d1 = datetime.date(2019, 1, 29)
print(d1)

d2 = d1.replace(year=2018, month=2, day=28)
print(d2)

print(d1-d2)

t1 = datetime.time(15,45,20)
print(t1)

t2 = t1.replace(14,44,19)
print(t2)

# TIME IT #

import timeit

print(timeit.timeit('-'.join(str(n) for n in range(100)),number = 1000))

import re

split_term = '@'
phrase = "What is your email? is it Hello@gmail.com"
a = re.split(split_term,phrase)
print(a)

print("Hello World".split())

print(re.findall('Match'.lower(),'Here is one match, Here is another match match'))