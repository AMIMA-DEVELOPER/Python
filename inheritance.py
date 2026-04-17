#Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.

class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name= name
        self.max_speed= max_speed
        self.mileage= mileage

class bus(vehicle):
    pass
School_bus= bus("School volvo",180,12)
print("vehicle name:",School_bus.name ,"and speed:",School_bus.max_speed,"and it's mileage",School_bus.mileage)

#Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number

class bird:
    def __init__(self):
        print("Brid is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("SWIM FASTER")

class Penguin(bird):
    print("Penguin")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("RUN FASTER")
peggy =  Penguin()
peggy.whoisThis()
peggy.run()
peggy.swim()




        
