#class IOString ():
 #   def __init__(self):
  #      self.str1 = ""

   # def get_String(self):
    #    self.str1 = input("Enter string: ")

  #  def print_String(self):
 #       print("Result is  :",self.str1.upper())

#str1 = IOString()

#str1.get_String()
#str1.print_String()


#Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!

class Employee:
    def __init__(self):
        print("Employee created!")

    def __del__(self):
        print("destructor called")

def Create_obj():
    print("Making objects.............")

    obj= Employee()
    print("function end....")
    return obj

print('Calling create obj() funtion.......')
obj = Create_obj()
print("program ends........")

    



