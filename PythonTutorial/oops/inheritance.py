'''
Inheritance: Child class acquiring the properties of Parent Class
1. Single level inheritance
2. Multi-level inheritance
3. Multiple inheritance
'''
class GrandFather:
    def display_gf(self):
        print("This is a GF method")
        
    def watch(self):
        print("This is GF watch")

class Father(GrandFather):
    def display_f(self):
        print("This is a Father method")
    
    def watch(self):
        print("This is Father's watch")
    
class Mother():
    def display_m(self):
        print("This is a Mother Method")
        
    def watch(self):
        print("This is Mother's watch")
        
class Child(Mother, Father):
    def display_c(self):
        print("This is a child method")
    
    def watch(self):
        print("This is Child's watch")
    
    
        
ajja=GrandFather()
# ajja.display_gf()
# ajja.watch()

appa=Father()
# appa.display_f()
# appa.display_gf()
# appa.watch()

nanu=Child()
# nanu.display_c()
# nanu.display_f()
# nanu.display_gf()
# nanu.display_m()
nanu.watch()

print(Child.mro()) #Method Resolution Order