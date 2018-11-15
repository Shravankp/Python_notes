#python:

var1 , var2 = input().split()
l = [1,2,3,4]
a,b,c,d = l      #list,tuple,sets can be directly assigned to equal no of variables
## a variable outside function can be accessed in the function but cant be modified ,
## to modify either use global or assign it to another var and return it

##The method strip() returns a copy of the string in which all space chars have been stripped from the beginning and the end of the
##string(default whitespace characters).

#in python everything are objects even functions , a function object can be referenced by more than one name eg:
def first(s):
    print(s)
first('Hello')
second = first
second('hi')
#Hello
#hi

## function that take other functions as arguments are also called higher order functions. eg:
list( map(int , x) )


# FILE :

file1 = open('file.txt','r').readlines()
#readlines()stores the contents of file.txt in LIST and is assigned to file1

file1 = open('file.txt','r')
#if file1 is printed it gives the same content of file as output
file1.close()

#csv - comma separated value or any delimiter
import csv               #only python file can be imported
with open('examples.csv') as csvfile:             # with operator is used for file operations , no need to close the file 
    readcsv = csv.reader(csvfile,delimiter = ',') #.reader for csv
##examples.csv has      1/2/2014,5,8,red
##                      1/3/2014,5,2,green
##                      1/4/2014,9,1,blue
    dates = []
    color = []
    for row in readcsv:
        
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    try:
        whatColor = input('What color do you wish to know the date of?:')
        if whatColor in colors:
            coldex = colors.index(whatColor.lower())
            theDate = dates[coldex]
            print('The date of ',whatColor,'is:',theDate)
        else:
            print('color not found')
    except Exception as e:
        print(e)

    print('continuing')


f.write("my first file\n")
f.read(10)  # read first 10 characters if size not specified read till EOF
f.readline() # reads line by line i.e till \n is found
f.seek(0) # to move cursor to required position (here initial(0))
f.tell() # to get current cursor position


#Exception
## exceptions can be explicitly raised by using raise keyword. if(..): raise valueError("not a +ve number")
## user defined exceptions can be raised by deriving 'exception' class (which is also a base class for all built-in exceptions)


#*args and **kwargs:
#*args allow you to pass variable number of arguments to a function 
#**kwargs allows you to pass variable number of arguments to a function but key-value pairs

#1.
def test_var_args(f_arg, *argv):          #accepts variable no of arguments
    print("first normal arg:", f_arg)
    for arg in argv:                       
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

#2.
def greet_me(**kwargs):                     #accepts variable no of arguments in form of key-value pairs or dictionary
    for key, value in kwargs.items():       
        print("{0} = {1}".format(key, value))

greet_me(name="yasoob")
# name = yasoob

#3.
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    #or
def test_args_kwargs(*args):  # for variable no of arguments
    i = 0
    for arg in args:
        i += 1
        print(" arg ",i," is ",arg)

    
# first with *args
args = ("two", 3, 5)
test_args_kwargs(*args)   
#or: test_args_kwargs(*('two',3,5))
                            #*args and **kwargs need not be in function parameters only, it can be arguments also
                          #actually used to reduce code redundancy 
                            #i.e even if no of elements in args changes, the arguments in function call is not re-coded here
                          #when called without *, whole tuple is passed to a function as one parameter ,
                            #whereas with * it is considered as three elems 
#arg1: two
#arg2: 3
#arg3: 5

# now with **kwargs:
def test_args_kwargs(**args):  # for variable no of arguments of dictionaries
    i = 0
    for key,value in args.items():
        i += 1
        print(" arg ",i," is ",key,'-',value)
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
#or test_args_kwargs(**{"arg3":3,"arg2":"two","arg1":5})
#arg1: 5
#arg2: two
#arg3: 3


##We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
##Since tuple are immutable, iterating through tuple is faster than with list.
##Strings are immutable



#line justify

#wordlen = 20
'hello world'.ljust(wordlen,'-') #2nd param is space-fill parameter
#'hello world---------'
'hello world'.center(wordlen*2) #second arg is taken as default i.e space
# '              hello world               '
('hello world'.rjust(wordlen*2 , '@')).center(wordlen*3)
#'          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@hello world          '




#NAMESPACE: 
a = 2                      # everything in python is object , so here 2 is an object with 'a' as reference or name to object
# Output: id(a) = 10919424 # object's or references's address can be found by using id()
print('id(a) =', id(a))

a = a+1
# Output: id(a) = 10919456
print('id(a) =', id(a))

# Output: id(3) = 10919456
print('id(3) =', id(3))

b = 2
# Output: id(2)= 10919424
print('id(2) =', id(2))

#built-in(-5 to 256) namespace , global namespace ,local namespace


#CLASSES AND OBJECTS:
class First:
    """ this is doc string """
    a = 10
    def fi(self):
        print('hello')
print(First.a)
#10
print(First.fi)          
#<function First.fi at 0x01331B28>
print(First.__doc__)      #not First.__doc__()
#this is doc string 

First.fi()            # this is function object, if self is declared in func params then this cmd doesn't work 
#hello
First.__doc__
#this is doc string  

ob = First()            # ob is a new reference (or instance object)  to object First() 
ob.fi()                # this is method object
#hello
## whenever an object calls its method, the object itself is passed as the first argument.
## So, ob.fi() translates into First.fi(ob)

#2.
class ComplexNumbers:
    def __init__(self,r=0,i=0):  #__init__(self) is a constructor
                                #Class functions that begins with double underscore (__) are called special functions
        self.real = r
        self.imag = i
    def getdata(self):
        print("{0}+{1}j".format(self.real,self.imag))
    

ob = ComplexNumbers(10,3)
ob.getdata()
#10+3j
ob1 = ComplexNumbers(10)
ob1.getdata()
#10+0j
ob1.attr = 10
print(ob1.attr)

del ob1.imag
del ob1.getdata()
del ob1             #On the command del ob1, this binding is removed and the name ob1 is deleted from the corresponding namespace.
                    #The object however continues to exist in memory and if no other name(reference) is bound to it,
                    #it is later automatically destroyed (known as garbage collection)


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [ 0 for i in range(no_of_sides) ]
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
        print(self.sides)
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def area(self):
        a , b , c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(area)
ob = Triangle()
ob.inputSides()
ob.area()

isinstance(ob,Triangle)
#True
isinstance(ob,Polygon)
#True
isinstance(ob,object)
#True
issubclass(Triangle,Polygon)
#True
issubclass(Triangle,object)
#True

MultiDerived.__mro__                        # method resolution order
##(<class '__main__.MultiDerived'>,    here MultiDerived is user-defined class which has multiple parent class
## <class '__main__.Base1'>,            so any attribute is searched in the specific order as specified by __mro__
## <class '__main__.Base2'>,                uses depth-first , left-right algos to search funcs , attributes
## <class 'object'>)


#Operator overloading :
# if objects are to be added or sub or mul these special functions should be overloaded
##Addition	    p1 + p2	p1.__add__(p2) --> class.__add__(p1,p2)
##Subtraction	    p1 - p2	p1.__sub__(p2)
##Multiplication    p1 * p2	p1.__mul__(p2)
def __add__(self,other):
    a = self.x + other.x 
    return a

#Iterators :
## for implements two special methods , __iter__() and __next__() , 
class PowTwo:                               
    """Class to implement an iterator
    of powers of two"""
                                            
    def __init__(self, max=0):              # for iterator's internal working may be diff but it should have these functions
        self.max = max                      # for is a keyword which calls these funcs , as everyclass derives Object class

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration          # exception
        
a = PowTwo(4)                               # so 4 is passed to __init__() function
i = iter(a)                                 # returns object to i which has n=0, observe how special functions are called without __
#or a = iter(PowTwo(4))
next(i)
next(i) # special_func(object)
next(i)
#1
#2
#4
## The built-in function iter() can be called with two arguments
## where the first argument must be a callable object (function) and second is the sentinel( termination value)
# so a class with iter and next can be used instead of for loop 

##      str() or __str__()	                      repr() or __repr__()
## - make object readable	        - need code that reproduces object
## - generate output for end user	- generate output for developer
## - used with print(object)            - used as secondary preference (when pressed object↵)

# built-in functions __iter__() & __next__() , takes iterable objects and converts it into iterator
# every generator is an iterator

#Generator
##If a function contains at least one yield statement (it may contain other yield or return statements), its a generator function
def rev_str(my_str):
    for i in range(0,len(my_str))):
        yield my_str[i]
for i in rev_str("hello"):
    print(i)
#h
#e
#l
#l
#o

s = (x**2 for x in my_list)  # return generator object ( next(s) can be used .whereas list objects are not iterable)

# instead of PowTow discussed above simple code can be implemented using generators
def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
#generator returns an object which can be iterated
        
#A normal function to return a sequence will create the entire sequence in memory before returning the result.
#This is an overkill if the number of items in the sequence is very large. so generators are memory efficient
#3.
def cities():
    for city in ["Berlin", "Hamburg", "Munich", "Freiburg"]:
        yield city

def squares():
    for number in range(10):
        yield number ** 2

def generator_all_in_one():
    for city in cities():
        yield city
    for number in squares():
        yield number

def generator_splitted():
    yield from cities()
    yield from squares()

lst1 = [el for el in generator_all_in_one()]
lst2 = [el for el in generator_splitted()]
print(lst1==lst2)
#true         (['Berlin', 'Hamburg', 'Munich', 'Freiburg', 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]) both lst1 and lst2 have same o/p


#Closure :
def make_multiplier_of(x):
    def multiplicand(n):
        return x * n
    return multiplicand

times_3 = make_multiplier_of(3)  #returns the nested func of enclosed func

print(times_3(9))
#27

times_5 = make_multiplier_of(5)

print(times_5(9))
#45

#The cell object has the attribute cell_contents which stores the closed value.
print(times_5.__closure__[0].cell_contents)
#5

#2.
def polygon(n):
    no_of_sides = n
    def triangle(base,height):
        area = 0.5 * base * height
        return area
    def rectangle(width,length):
        area = width * length
        return area
    if n==3:
        return triangle
    elif n==4:
        return rectangle
    else:
        print('unknown polygon')

new_poly = polygon(4)
print(new_poly(3,5))
new_poly.__closure__[0].cell_contents



# We must have a nested function (function inside a function).
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.


#Decorators :

##A decorator takes in a function, adds some functionality and returns a new function.
def make_pretty(func):
    def inner():
        print("No I am altered")
        func()
    return inner

def ordinary():
    print("Original")

pretty = make_pretty(ordinary)
pretty()

#No I am altered
#Original

#usually in decorators:
ordinary()
#original
ordinary = make_pretty(ordinary)  #a new function has same name as the parameter function
ordinary()
#No I am altered
#original

# annotation form
@make_pretty                             #closure_function_name
def ordinary():                          #parameter function for closure
    print("I am ordinary")
#is same as
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)        #not make_pretty(ordinary())

#2.
def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

divide(2,4)
#"I am going to divide",2,"and",4
#0.5
## here no of parameter for nested func inside decorator(smart_divide) is same as other funcs(divide)

# General decorators:
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

#3.
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
#same as : printer = star(percent(printer))   i.e execution is done for percent() first then star()
printer("Hello")

##******************************
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
##Hello
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
##******************************

# @property:
#used for refactoring ,if some naming of variables changes ,here temperature is changed to _temperature

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)   #inside the class

##Any code that retrieves the value of temperature will automatically call get_temperature() instead of dictionary __dict__ look-up.
##Similarly, any code that assigns a value to temperature will automatically call set_temperature()

##An underscore (_) at the beginning is used to denote private variables in Python.

##property(fget=None, fset=None, fdel=None, doc=None)
##where, fget is FUNCTION to get value of the attribute, fset is FUNCTION to set value of the attribute,
##fdel is FUNCTION to delete the attribute and doc is a string
##A property object has three methods, getter(), setter(), and delete() to specify fget, fset and fdel

temperature = property(get_temperature_function , set_temperature_function)

#can be broken down as

temperature = property()
# assign fget
temperature = temperature.getter(get_temperature_function)
# assign fset
temperature = temperature.setter(set_temperature_function)

#using decorators , so the above example can be written as:
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):              #this function name does'nt matter
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):       #this function name does'nt matter
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

c = Celsius()
#Setting value
c.temperature = 37
#Setting value
print(c.to_fahrenheit())
#Getting vlaue
#98.600001

#mutation:
foo = ['hi']
poo = foo
poo += ['bye']
print(poo)
#['hi','bye']
print(foo)
#['hi','bye']
##Whenever you assign a variable to another variable of MUTABLE datatype, any changes to the data are reflected by both variables.
##The new variable is just an alias for the old variable.

def add_to(num,target=[]):    
    target.append(num)
    return target

add_to(1)
#[1]
add_to(2)
#[1,2]        not [2]
add_to(3)
#[1,2,3]      not [3]
##so never define default argument as mutable datatype
## In Python the default arguments are evaluated once when the function is defined, not each time the function is called.
##avoid by using example -> def add_to(num,target=None):    if target is None:  target=[]


