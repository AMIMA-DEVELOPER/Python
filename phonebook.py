import sys

def initial_phonebook():
    rows, cols = int(input("please enetr the initial no. of the contacts:   ")), 5
    
    phonebook= []
    print(phonebook)

    for i in range (rows):
        print("\nEnter contact %d deatils in following orders (ONLY) :"% (i+1))
        print("Note: *inidcate mandotary fields   ")
        print("*************************************************************************" ) 

        temp= []
        for j in range(cols):

           if j ==0:
               temp.append(str(input("Enter name* =   ")))
               if temp[j] == "" or temp[j] == ' ':  
                   sys.exit("Name is mandotary" )  


            
           if j ==1:
               temp.append(int(input("Enter number* =   ")))


           
           if j ==2:
               temp.append(str(input("Enter email =   ")))
               if temp[j] == "" or temp[j] == ' ':  
                   temp[j] == None


           
           if j ==3:
               temp.append(str(input("Enter birth date/month/year =   ")))
               if temp[j] == "" or temp[j] == ' ':  
                   temp[j] == None     

           
           if j ==4:
               temp.append(str(input("Enter category (family/work/friends) =   ")))
               if temp[j] == "" or temp[j] == ' ':  
                   temp[j] == None  

        phone_book.append(temp)  

    print(phone_book)
    return(phone_book) 

def menu():
               




                   

