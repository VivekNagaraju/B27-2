'''
List:
1. an empty list can be created
'''
'''
a=[] #1. an empty list can be created
print("a-->",a)
print(type(a))
b=[1,2,3,4] # 2. creation of list manually with elements
print("b-->",b)
'''
c=list(range(2, 21, 2)) #3. Creation list using built-in function
print("c-->",c)
'''
d=[1, 2.4, "abc", True] #4. List can be Heterogeneous 
print(d)
'''
'''
#4. Accessing the individual elements using indexing
print(c[5])
print(c[-5])
'''

#5. access using slicing operator
'''
#slicing using positive index
print(c[1:5])
print(c[:5])
print(c[5:])
print(c[5::])
'''
'''
#slicing using negative index
print(c[:-5])
print(c[-2:-9:1])
print(c[-2:-9:-1])
print(c[::1])
print(c[::-1])
'''
c[4]=15
print("c after modifying-->",c) #6. List can be modifiable
