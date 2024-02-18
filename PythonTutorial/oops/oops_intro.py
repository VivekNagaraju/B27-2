'''
Created on 20-Jan-2024

@author: admin
'''

class CarClass():
    def __init__(self, name, color):
        self.name=name
        self.color=color
    
    def display_details(self):
        print(f"My car is {self.name} and it is  {self.color} in color")
    
    def move_forward(self):
        print(f"My {self.name} car is moving forward")
        
car1=CarClass("Swift", "White")
car1.display_details()


car2=CarClass("Brezza", "Black")
car2.display_details()
car1.display_details()
print(car1.name)
print(car1.color)
print(car2.color)
print(car2.name)
print(type(car1))
print(type(car2))