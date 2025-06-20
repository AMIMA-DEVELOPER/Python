# write a program to create a class Parrot and perform the following tasks 
# - Create a class variable species, 
# Create a constructor that has instance variables - name and age, 
# Create instances of class Parrot, passing arguments as well, Print Class variable by accessing it, Print Instance #variables as well.


class Parrot:
    species="bird" 
    def __init__(self,name,age) :
        self.name=name
        self.age=age

Pr=Parrot("mit",7)
Tr=Parrot("bit",8)
print(Pr.name,"is a",Pr.species)    

print(Tr.name," is ",Tr.age," years old")    
print(Pr.name,"efone")


#Write a Python class named Rectangle with a length and width and a method that computes the area of a rectangle. Display the dimensions and calculated area of the rectangle as well.

class rectangle:
    def __init__(self,length,width):   
        self.length= length
        self.width= width
    def area(self):
        print("AREA OF THE RECTANGLE IS", self.length*self.width)
         
length=int(input("Enter the length  "))
width=int(input("Enter the width    "))




r =rectangle(length,width)
r.area()        


#Print the peremeter and the area of the circle

class circle:
    def __init__(self,radius):
       self.radius= radius
    def peremeter(self):
    
        print("The peremeter of the circle is  " ,2*3.142*self.radius)

    def area(self):
        print("the area of the circle is" ,3.142*self.radius*self.radius)


Radius= int(input("The value for the radius  "))
C= circle(Radius)
C.peremeter()
C.area() 

        
          
