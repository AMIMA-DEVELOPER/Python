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

    print("*******************************************************")
    print("\t\t\t Smart phone Directory")
    print("*******************************************************")
    print("\t You can now perform the following operations on this phone book")
    print("1. Add a new contact")
    print("2. Remove an existinng contact")
    print("3. Dlete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit Phonebook")

    choice= int(input("Enter your choice  "))

    return choice

def add_contact (pb):
   
   dip=[]
   for i in range (len(pb[0])):
    if i == 0:
        dip.append(str(input("Enter name  ")))
           
    if i == 1:
        dip.append(int(input("Enter number  ")))  

    if i == 2:
        dip.append(str(input("Enter email-address  ")))

    if i == 3:
        dip.append(str(input(" Enter date of birth/month/year  ")))

    if i == 4:
       dip.append(str(input("Enter category(/family/realtion/work/other)")))  
   
   pb.append(dip)

   return pb            

def remove_existing (pb):

    query = str(
        intput("please enter the name of the contact you wish to remove: "))

    temp = 0

    for i in range (len(pb)):
        if query == pb [i][0]:
            temp +=1

            print(pb.pop(i))  

            print("This query has now been removed")

    if temp ==0
        print("sorry , you have enterred an invalid query. \n please recheck and try again later")

        return (pb)
    
    def delete_all(pb):

     def search_existing(pb):
         choice = int(input("Enter search criteria\n\n\n 1. name\n2. Number\n3. Email-id\n4. DOB\n5. Category(family\friend\work\others)\ \nplease enter:  "))

         temp =[]  
         check = -1

         if choice == 1:
             query = str(input( "please enter the name of the contact ypu wish to search" )) 
             for i in range(len(pb)):
                 if query == pb[i][0]:
                     check = i
                     temp.append(pb[i])

         elif choice == 2:
             query = int(input( "please enter the number of the contact ypu wish to search" )) 
             for i in range(len(pb)):
                 if query == pb[i][1]:
                     check = i
                     temp.append(pb[i])    
         elif choice == 3:
             query = str(input( "please enter the email- address of the contact ypu wish to search" ))
             for i in range(len(pb)):
                 if query == pb[i][2]:
                     check = i
                     temp.append(pb[i]) 

         elif choice == 4:
             query = str(input( "please enter the DOB of the contact ypu wish to search" ))
             for i in range(len(pb)):
                 if query == pb[i][3]:
                     check = i
                     temp.append(pb[i]) 

         elif choice == 5:
             query = str(input( "please enter the email- address of the contact ypu wish to search" ))
             for i in range(len(pb)):
                 if query == pb[i][4]:
                     check = i
                     temp.append(pb[i]) 

         else:
             print("invalid search")
             return -1
         if check ==-1:
             return -1
         else:
             display_all(temp)
             return check
         
def display_all (pb):
    if not pb:
        print("list is empty: []")
    else:
        for i in range (len(pb)):
            print(pb[i])

def thanks():
    print("**************************************************")
    print("thank you for using our smart phone directory system.")
    print("Please visit again!!")
    print("**************************************************")
    sys.exit("goodbye")

    print("..................................................")
    print("Hello, WElocome to our directory system")
    print("You may proceed to explore!!")
    print("..................................................")
ch=1
pb= initial_phonebook()
while ch in (1,2,3,4,5):
    ch = menu()
    if ch ==1:
        pb = add_contact(pb)

    elif ch ==2:
        pb = remove_existing(pb)

    elif ch ==3:
        pb = delete_all(pb)
    
    elif ch ==4:
        d = search_existing contact
        if d == -1:
            print("the contact does not exist, Try again")
    elif ch ==:
        pb = remove_existing(pb)



                     

