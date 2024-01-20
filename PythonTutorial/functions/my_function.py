'''
Functions:
1. Creating a function with or without parameter
2. Calling a function with or without parameter
3. Creating a function with parameter having default value
'''
'''
def welcome(name=""):
    print(f"Hi {name}...!! Welcome to iQuest!!")

welcome("Manoj")
welcome("Gouthami")
welcome()
'''
'''
a=1
b=2
c=a+b
print(c)

a=5
b=4
c=a+b
print(c)

a=7
b=6
c=a+b
print(c)
'''

def add(a=0, b=0): # formal arguments
    c=a+b
    d=a-b
    # print("a", a)
    # print("b", b)
    print(c)
    print(d)
    # return c, d

# x, y=add(2, 4)# actual arguments # positional arguments 
# print(x)
# print(y)
# print(add(5, 3)) 
# add(b=4, a=5) # Keyword arguments

def add2(*a): # Variable length argument
    print(sum(a))   
    
# add2(1, 22, 3, 4, 5)
# add2()
# add2(a=1, b=2, c=3)

def display(**a): # keyword variable length argument
    print(a)
    
# display(a=1, b=2, c=3)

def display2(*a, **b):
    print(a)
    print(b)

# display2(1, 2, 3, a=1, b=2, c=4)