'''
Created on 03-Feb-2024

@author: admin
'''
print(2+3)
print(4/3)
# print(4/0)
# print(4/"abc")
try:
    print(4/"abc")
    
except ZeroDivisionError as ze:
    print("ZE Specific except block:",ze)
         
except TypeError as te:
    print("TE Specific except block:", te)
       
except Exception as abc: # default except block
    print("default except block:",abc)
    
print(6*2)
