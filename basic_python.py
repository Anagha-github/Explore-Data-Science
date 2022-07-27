#Comment
from typing import Tuple


x = 4 #x is a variable
y = int(5) #Casting is to specify the data type while defining a variable
z = int(5.3) #Casted to 5
print(type(x)) #Get the type of the variable

""" Group comment
Illegal variable names
2myvar = "John"
my-var = "John"
my var = "John"
"""
#Leagal or common variable names
camelCase = "first letter of the first word small"
PascalCase = "first letters of all the words big"
snake_case = "all small but words separated"

#Many to many
a,b,c = 1,2,3
#one to many
d = e = f = 4
#unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)

#Print statement with , and +
x= "John"
y= "Tom"
print(x,y) #with space
print(x+y) #without space
z= 3
#print(y+z) is error
print(y,z)
print(y.format(z))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Global variable and keyword
x = "awesome" #global variable
def myfunc():
  global x #global keyword to make inner variable global
  x = "fantastic"
myfunc() #value of x globally changed from awesome to fantastic from within a func
print("Python is " + x) #python is fantastic

#Datatype
x = 1j
print(type(x)) #Complex
x = ["apple", "banana", "cherry"]#list
x = ("apple", "banana", "cherry")#tuple
x = {"apple", "banana", "cherry"}#set
x = {"name" : "John", "age" : 36}#dict
x = 35e3 #float 35000.0 
y = 12E4 #float 120000.0 
z = -87.7e100 #float -8.77e+101

#Print a paragraph
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#String as array
print(a[3])#e
#String in loop
b = "cat"
for i in b:
    print(i)
print("Lorem" in a)#True
print("sed" not in a)#False
print(a[:5])#slice from begining
print(a[7:])#slice to end
print(a[3:7])#slice a section
print(a[-10:-4])#slice from end

#Modifying
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print(a.upper())
print(a.lower())
print(a.replace("H", "J"))
print(a.split(","))#returns a list

"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

#List
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #['apple', 'watermelon']
thislist.insert(2, "watermelon")
thislist.append("orange")
thislist.insert(1, "orange")
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #or list3 = list1 + list2 or 
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist.remove("mango") # thislist.pop(1)
thislist.pop() # removes the last one
del thislist[0]
thislist.clear()#variable remains with no content []

#Comprehension : to make a new list from an existing list based on condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]#Return "orange" instead of "banana"

#Sorting a list
fruits.sort()#alphabetically
thislist = [100, 50, 65, 82, 23]
thislist.sort()#numerically
thislist.sort(reverse = True)#descending, works for both number and alphabets

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)#sorts capital words before small words.. to avoid this use the below:
thislist.sort(key = str.lower)#key helps to do the calculation without altering the content itself
print(thislist)
thislist.reverse()#just reverses the existing order

mylist = thislist.copy()#same as mylist = list(thislist)

#Tuple
thistuple = ("apple",) #for one item tuple ("apple") is not a tuple.coma is important
#tuples are immutable, so to change a tuple, convert tuple to list and change list and convert back to tuple

#Sets: Unordered and unchangeable, items cannot be indexed, no duplicates
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
mylist = ["kiwi"]
thisset.update(mylist)

thisset.remove("banana")#raises error if banana does not exist
thisset.discard("banana")#if banana does not exist, discard does not raise error

x = thisset.pop()#will remove last item, but sets are unordered so we wont know which item is removed
thisset.clear()#empties set, but set still exists
del thisset #deletes the set

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)#have to store as a new set
set1.update(set2)#addes to set1

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)#keeps only the ones that are common among both sets
z = x.intersection(y)#same as above but stores to z
x.symmetric_difference_update(y)#keep all except the common
z = x.symmetric_difference(y)

#Dictionaries: Python version 3.7, dictionaries are ordered
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")
x = thisdict.keys()
x = thisdict.values()
thisdict["color"] = "white"
thisdict["year"] = 2020 #or
thisdict.update({"year": 2020})

thisdict.popitem()#remmoves the last key values pair
thisdict.pop("model")#specific
del thisdict["brand"]
thisdict.clear()#empty dict
del thisdict#dict does not exist

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
for x in thisdict.values():
  print(x)
for x in thisdict:
  print(thisdict[x])#also prints all values
for x, y in thisdict.items():
  print(x, y)#to loop through key and values
  
mydict = thisdict.copy()#or mydict = dict(thisdict)

#oneline if else statement
a = 2
b = 330
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")
#and or 
if b > a:
  pass
#break statement can stop the loop even if the while condition is true
#else statement can run a block of code once when the condition no longer is true

#functions
def my_function(*kids):#when we dont know how many values are passed to this argument.*
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")#key value, so the order of values does not matter

def my_function(**kid):#do not know how many keyword arguments that will be passed into the fn
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")#function will receive a dictionary of arguments

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function()#uses the default value
my_function("Brazil")

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)

#Lambda function: used when an anonymous func is required for a short period of time.
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)#value for n
print(mytripler(11))#value for the lambda func, 33



