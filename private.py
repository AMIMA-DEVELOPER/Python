#Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.


# class myclass:
#     __privateVar = 27;
    

#     def __privateMeth(self):
#         print("I am inside class myclass")

#     def hello(self):
#         print("Private Variable value",myclass.__privateVar)

# foo =  myclass()
# foo.hello()
# foo.__privateMeth

#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.


# class computer:

#     def __init__(self):
#         self.__maxprice = 7000

#     def sell(self):
#         print("selling price: {}".format(self.__maxprice))

#     def setMaxprice(self,price):
#         self.__maxprice = price

# c =  computer()
# c.sell()

# c.__maxprice = 1000
# c.sell()

# c.setMaxprice(1000)
# c.sell()

# Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.

# class Point:
#     def __init__(self, x =0,y=0):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return "({0},{1})".format(self.x , self.y)
    
# p1 = Point(2,3)
# print(p1)
        

class Number:
    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return Number(self.value + other.value)
a = Number(5) 
b = Number(10)
c = a + b
print(c.value) 

