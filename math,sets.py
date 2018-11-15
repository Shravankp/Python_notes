import statistics 
s = [1,2,3,4]
x = statistics.mean(s) #variance, mode,median, stdev

from statistics import variance as v , mean as m
x = v(s)




(1.1 + 2.2) == 3.3
#False
#Turns out decimal fraction 0.1 will result into an infinitely long binary fraction of 0.000110011001100110011...
#so we use decimal module which has upto 15 decimal precision

from decimal import Decimal as d
print(d(1.1+2.2))           # 3.300000000000000266453525910037569701671600341796875
print(d('1.1') + d('2.2'))  # use string to get usual output i.e 3.3
print(d('1.1+2.2'))         # error

from fractions import Fraction as f
print(f(1.5))
# 3/2
print(f(1.1))
# 2476979795053773/2251799813685248
print(f('1.1'))
# 11/10

import math
print(math.pi)
# Output: 3.141592653589793
print(math.cos(math.pi))
# Output: -1.0
print(math.exp(10))
# Output: 22026.465794806718
print(math.log10(1000))
# Output: 3.0
print(math.sinh(1))
# Output: 1.1752011936438014
print(math.factorial(6))
# Output: 720

import random
print(random.randrange(6,14))
#11
x = [3,5,2,4]
print(random.choice(x))
#5
random.shuffle(x)
print(x)
#[5,2,3,4]
print(random.random())
#0.67586467987676

from itertools import product as p , permutations as pe , combinations as co
print(list(p([1,2,3],repeat=2))) #repeat is length of each tuple
#[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
print(list(p([1,2],[2,3,4])))
#[(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4)]
print(list(pe([1,2,3],2)))
#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(list(co([1,2,3],3)))
#[(1, 2, 3)]




#SETS: are mutable but frozen sets are immutable
x = set("A Python Tutorial")
# {' ', 'A', 'P', 'T', 'a', 'h', 'i', 'l', 'n', 'o', 'r', 't', 'u', 'y'}

x = set(["Perl", "Python", "Java"])             #whole list can be converted to set
#{'Java', 'Perl', 'Python'}

cities = set((["Python","Perl"], ["Paris", "Berlin", "London"])) # indivisual mutable elements cannot be converted to set
# error


my_set.add(2)
print(my_set)
# Output: {1, 2, 3}


my_set.update([2,3,4])
print(my_set)
# ADD multiple elements or UPDATE
# Output: {1, 2, 3, 4}

my_set.update([4,5], {1,6,8})
print(my_set)
# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}

my_set = {1, 3, 4, 5, 6}
my_set.discard(4)
my_set.remove(6)  # difference between these two is, while using discard() if item does not exist then remains unchanged
                    # in remove() throws an error
my_set.pop() #deletes and returns
c1 = my_set.copy()
my_set.clear()

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
c = A|B #or
c = A.union(B)

c = A & B #or A.intersection(B)

c = B - A #or B.difference(A)

c = A^B #or A.symmetric_difference(B)

A.isdisjoint(B) #False

##Sets being mutable are unhashable, so they can't be used as dictionary keys
##On the other hand, frozensets are hashable,immutable so can be used as keys to a dictionary
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList) , sorted(pyList,reverse=True)
#['a', 'e', 'i', 'o', 'u']['u', 'o', 'i', 'e', 'a']

random = [(2, 2), (3, 4), (4, 1), (1, 3)]
sortedList = sorted(random, key=takeSecond)
#[(4, 1), (2, 2), (1, 3), (3, 4)]

li = [True,True,False] #True=1 , False=0 , -True=-1
sum(li)
#2
li = [True,-True,False]
sum(li)
#0

eval('s.{0}({1})'.format(*input().split()+[''])) # s is set , * converts argument into positional arguments
                                    #i.e inputs are separated into no of arguments , [''] is used to support pop(a return value)
#input -> remove 2
#         pop
#         discard 3


