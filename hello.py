print("hello world\n") 
x=float(8)
y='wow'
if x > 7 : 
    print("true")
    print(x)
else :
    print("false")
    print(y)

X="55"
print(type(x))
print(type(y))
#many values to multiple variables
l, m, n = "Audi", "Skoda", "Mercedes Benz"
print(l)
print(m)
print(n)
#one value to multiple variables
w= r= s = "Fiat"
print(w)
print(r)
print(s)

#colloections or lists 
fruits = ['mango','apple','grapes']
print(fruits)
l,m,n = fruits
print(l,m,n)
print(l+' '+m+' '+w)

a= 1
b= 6
print(a+b)


#functions 

def func(): 
    global y
    global z
    z= 'wonderful'
    y ='awesome'
    X = 'amazing' 
    print('Python is',y,',',z,'and',X)


func()
print(y)
print(X)
print(z)

import random

print(random.randrange(1,10))

greeting = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(greeting)
print(greeting[0])

for f in 'beatiful':
    print(f)

print(len(greeting))

txt = "The best things in life are free!"
print("good" in txt)
print("free" in txt)
if 'life' in txt:
    print('yes life is present')
if 'cry' not in txt:
    print('dont you ever cry')
#slicing strings
#last postion not included 
print(greeting[1:7])
#slice from the start 
print(greeting[:6])
#slice to end
print(greeting[100:])


v=' Taehyung, V '
print(v)
print(v.upper())
print(v.lower())
print(v.strip())
print(v.replace('T','J'))

v = v.split(",")
print(v)

age = 22
text = "My name is John, and I am {}"
print(text.format(age))

quantity = 3
itemno = 567
price = 49.95
#formatting
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#indexed formating 
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print("I don\'t really gaf")
print("We are the so-called \"Vikings\" from the north.")
k = "\x48\x65\x6c\x6c\x6f"
print(k) 

'''
these are false values 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''

class myclass():
  def __len__(self):
    #if the __len__ function returns a flase value then the object will have a flase 
    #value otherwise it will be a true value
    return 1

myobj = myclass()
print(bool(myobj))


# a function reurns either false or true 
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

o = 200
print(isinstance(o, int))
print(isinstance(o, str))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#shortcut for looping 
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

c= json.loads(y)
print(c["age"])

username = input("Enter username:")
print("Username is: " + username)

print('i am learning Python'\
      .capitalize())

dates = ['2023-06-19', '2023-06-20', '2023-06-21']
date = '2023-06-19'

if [date != x for x in dates]:
    print("Date is not present in the list.")
else:
    print("Date is present in the list.")





















