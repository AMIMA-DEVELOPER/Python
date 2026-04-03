#Write a program to create a class with the name Student and perform the following tasks - 1. Declare a variable grade 2. Print a sentence inside the class 3. Create an object of class student and see the output

class student:
    grade = 2
    print("HELLO WORLD! I am a student of grade",grade)

ob = student()

#Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object

class car:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = car(120,66)

print("MODEL MAX SPEED",modelX.max_speed)


print("MODEL MILEAGE",modelX.mileage)

#Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well

class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

PT = parrot("Tilly",7)

print("THE NAME OF THE PARROT IS ",PT.name , "and It's age is",PT.age, "It belong the species of ",PT.species)
        
