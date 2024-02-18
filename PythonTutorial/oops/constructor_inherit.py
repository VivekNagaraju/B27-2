'''

'''
class GrandFather:
    def __init__(self, name, age=None):
        self.name=name
        self.age=age
        # print(f"Object is created with name:{self.name} and age:{self.age}")
        
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
class Father(GrandFather):
    def __init__(self, name, age, adhaar_id):
        super().__init__(name, age)
        self.adhaar_id= adhaar_id
        # print(f"Object is created with name {self.name}, age {self.age} and adhaar_id {self.adhaar_id}")
        
    def display_details(self):
        super().display_details()
        print("Adhaar ID:", self.adhaar_id)
        

        
        
ajja=GrandFather("Ajja", 99)
ajja.display_details()
# print(dir(ajja))

appa=Father("Appa", 69, 123)
appa.display_details()
