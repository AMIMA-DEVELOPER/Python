# write a program to create a class Parrot and perform the following tasks 
# - Create a class variable species, 
# Create a constructor that has instance variables - name and age, 
# Create instances of class Parrot, passing arguments as well, Print Class variable by accessing it, Print Instance #variables as well.


class Parrot:
    species="bird" 
    def __init__(self,name,age) :
        self.name=name
        self.age=age

Pr=Parrot("mithu",7)
Tr=Parrot("bithu",8)
print(Pr.name,"is a",Pr.species)    
print(Tr.name," is ",Tr.age," years old")    

