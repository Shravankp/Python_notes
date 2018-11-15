#os and sys:
import os
help()
help(os)

import os
curdir = os.getcwd()
print(curdir)

os.mkdir('newdir')
os.rename('newdir','newdir1')
os.rmdir('newdir1')

        
import sys     #this module is used to get arguments from cmdline or anything outside 
print(sys.argv)
if len(sys.argv) > 1: 
     print(int(sys.argv[1])+int(sys.argv[2]))
#['new.py', '5', '5']
#10

def my(arg):
    print(arg)
my(sys.argv[1])  # so here we are accessing the argument given in cmdline and passing it to a function using python





#urllib
#can be used to parse values into the url
import urllib
x = urllib.request.urlopen('https://www.google.com/') #but these stmts are considered as call from programs ,
print(x.read)                                           #so these requests are forbidden

##Breaking a data block into smaller chunks by following a set of rules,
##so that it can be more easily interpreted, managed, or transmitted by a computer.

#1.
import urllib.request
import urllib.parse
url = 'https://www.google.com/search'
values = {'q' : 'python programming tutorials'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)

#2.
import urllib
try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a person who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)#is used to alter the url requested
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))


#3.
import re
import urllib.request
import urllib.response

url = 'http://pythonprogramming.net'
values = {'s':'basics',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
req = urllib.request.Request(url,data,headers = headers)
resp = urllib.request.urlopen(req)
respData = resp.read()
#print(respData) all source code data
paragraphs = re.findall(r'<p>(.*?)</p>' ,str(respData))
for each in paragraphs:
    print(each)



#Pickling:
##Pickling is a way to convert a python object (list, dict, etc.) into a character stream.Converting stream to object is depickling
##The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.
import pickle
example_dict = {1:'hi',2:'how', 3:'are',4:'you?'}
pickle_file=open('pickle_in','wb') #write byte
pickle.dump(example_dict,pickle_file)
pickle_file.close()
pickle_file=open('pickle_in','rb') #read byte
ex=pickle.load(pickle_file)
pickle_file.close()
print(ex)


#eval and exec:
## eval("2+2") - When you need the value of an expression
## exec(' print("hello world") ') - to excecute commands exec acts as a compiler
x = eval(input("Enter the expression"))
#Enter the expression 5+6-8
x
#3

list_str = "[5,6,2,1,6]"
list_str = exec(list_str)
print(list_str)
#returns none , bcuz exec doesn't evaluates it compiles , so list_str is taken as new empty variable 

exec('list_str = [1,3,2,1,3]') #these assignments cant be done using eval
print(list_str)
#[1,3,2,1,3]

exec("""
def test():
    print('ooooo yes!!')
""")
test()
#ooooo yes!!




#lambda:
#Python has two tools for building functions: def and lambda
def g(s):
    return s**2
print(g(2))
#is same as..
g = lambda s:s**2
print(g(2))
#lambda returns the result same as functions




#map()
#map() applies a function to all the items of a given input_list i.e map() is an iterative thing
#1.
items = ['1','3','4','5']
int_items = list(map(int,items)) # converts every elements of items into integer list
squared = list(map(lambda x:x**2 ,int_items)) # function or anonymous function as 1st argument ,second arg is iterable


#2.
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add] # we aren't using multiply() or add()
for i in range(5):
    value = list(map(lambda x: x(i), funcs))# x takes the values of funcs
    print(value)
# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]



#filter:

num_list = range(-5,5) # this is actually a valid stmt. Also the following can be used
#range(-5,5)
num_list = list(range(-5,5))
#[-5,-4,-3,-2,-1,0,1,2,3,4]

less_thanzero = list(filter(lambda x:x<0 ,num_list))
# [-5, -4, -3, -2, -1]
#creates elements for which the input function returns True

num_list = range(-5,5)
less_thanzero = list(map(lambda x:x<0 ,num_list))
#[True, True, True, True, True, False, False, False, False, False]
#map() just evaluates and returns everything , filter evals and return only true solutions



# yield keyword:
# used as return keyword when using generators
#( generators - iterables that generates only one value at a time , kind of linked list) next() can be used for next elements
g = (2**x for x in range(2)) # generator expression- () , listcomp- [] , dictionary_comprehension- {}
next(g)
#0
next(g)
#2
next(g)
# error
print(g)
#[]

def generator():              #generator function or u can use generator expression as above
    for i in range(6):
        yield i*i          # if return used here , loop is executed only once
                            # saves space as no need to store values in separate list

for i in generator():
    print(i)
#prints 0 to 25 line by line
# if generators are used , none of the list operations can be performed i.e + and ..

#pdb (python debugger):
#pdb is used to trace the program by setting break points in the program and running some cmds at break points
import pdb
pdb.set_trace() #as soon as this cmd is called , control goes to pdb prompt .
               #some of the cmds are l(ist),n(ext),s(tep),q(uit)

#speed:
# lc > ge > for > map
# dc for dictionaries
# ge are memory or space efficient
