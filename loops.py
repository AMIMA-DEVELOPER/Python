#LOOPS
for i in range (1,7):
    for x in range (i):
        print("$",end=" ")
    print("\n")    

#Reverse pattern

for i in range (7,1,-1):
    for x in range (i,1,-1):
        print("@",end=" ")
    print("\n")

#Write a program to find out the denominations of notes of 2000, 500, 200, 100, 50, 20, and 10 for the total amount of money entered by the user.

def no_notes(a):
    x = [5000, 1000 , 500, 100, 50, 20 , 10]
    q= 0
for i in range(7):
      C = x[i]
      q= a//C
      print("Notes of {} = {}". format(C,q))
      a = a%C
amount= int(input("Enter total amount "))
no_notes(amount)

