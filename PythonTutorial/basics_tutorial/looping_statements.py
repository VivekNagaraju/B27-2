'''
1. Looping statements: to execute any statements repeatedly
    a. while loop- until condition is satisfying
        - initialization
        - condition statement
        - increment/ decrement
    b. for loop- to iterate over the range or sequence
    
break, continue: loop controlling statements
'''

'''
position=1
while position<=5:
    
    
    age=int(input("Enter your age:"))
    if age>=13:
        print("Allow")   
    else:
        print("Don't allow")
    
    print("Position value:",position)
    position=position+1
    if position==3:
        continue
    print("new position value:", position)
'''
'''
count=1
while count<=5:
    print("Hello world!")
    
    if count==3:
        break
    count=count+1
'''
count=1
while count<=5:
    
    if count==3:
        count=count+1
        continue
    print(count)
    count=count+1
'''
for count in range(5):
    print("Hello world!")
    
'''
'''
index=0
a=[1,2, 4, 5, "abv", 3, 4, 5]
for i in a:
    if i=="abv":
        continue
    print(i)
'''
'''
for i in a:
    if i==5:
        print(index, i)
    index=index+1
    # if i=="abv":
    #     break
    # print(type(i))
    # print("Hello world!")
'''