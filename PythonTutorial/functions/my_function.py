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

def add(a, b): # formal arguments
    c=a+b
    print(c)

add(2, 3) # actual arguments # positional arguments  
add(b=4, a=5) # Keyword arguments
    