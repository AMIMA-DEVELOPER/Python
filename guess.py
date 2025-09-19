import random
import time

number= random.randint(1,100)

def intro():
    print("May I ask you for your name")

    global name

    name= input()
    print(name + ", we are going to pay a game, I am thinking of a number betweeen 1-100") 
    if(number%2==0):
        x='even'
    else:
        x='odd'
        print("\n This is an {} number".format(x))

    print("Go, ahead and guess!")
    time.sleep(.5)

def pick():
    guessesTaken=0

    while guessesTaken < 6:
        time.sleep(.25)

        enter= input("Guess: ")
        
        try:

            guess = int(enter)

            if guess <=100 and guess>=1:
                guessesTaken=guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                        print("The guess of the number that you have eneterd is too low")
                    if guess>number:
                        print("The guess odf the number you have enetered is too high.")

                    if guess != number:
                        time.sleep(.5)
                        print("try again")

                    if guess==number:
                        break

            if guess>100 or guess<1:
                print("silly! That number isn't in the range!")
                time.sleep(.25)

                print("please enetr a number between 1 and 100")
        except:
            print("I don't think that"+enter+"is a number.sorry")

    if guess== number:
        guessesTaken = str(guessesTaken)
        print('GOOD JOB,{}! You have guessed the right number in {} guesses'.format(name, guessesTaken))
playagain ="yes"
while playagain== "yes" or playagain=="y" or playagain=="Yes":

    intro()
    pick()
    print("Do you want to play again??")
    playagain= input()

  


