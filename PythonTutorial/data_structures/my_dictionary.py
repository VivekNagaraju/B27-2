'''
Created on 14-Jan-2024

@author: admin
'''
a={}
b={1:"Gouthami", 2:"Manoj", 3:"Vivek"}
print(b)
c={1:"Gouthami", 2:"Manoj", 3:"Vivek",3:"Akash"} # dictionary will not allow duplicate keys
print(c)
d={1:"Gouthami", 2:"Manoj", 3:"Vivek",4:"Vivek"} # dict  will allow duplicate values
print(d)
e=dict(one=1, two=2, gouthami=3, manoj="shgjs", four="ajlh")
print(e)
'''
a[1]="anb"
a[4]="hjsgvk"
print(a)
print(e["two"])
print(e.keys())
print(e.items())
f=e.fromkeys((1,2,3,4), "NA")
print(f)
print(e)
'''
e.popitem()
print(e)
e.pop("two")
print(e)
print(e.values())