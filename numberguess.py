import random
import time

number = random.randint(1,100)
def intro():
    print("May I ask for your name?" )
    global Name
    Name= input()
    print(Name + ", we are going to paly a guessing game")
    print("You have to guess a number between 1 till 100. With the help of my hints.")
    if (number%2==0):
        x = 'even'

    else:
        x = 'odd'

    print("\n This is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead! and Guess!")

def pick():

    guessTaken= 0

    while guessTaken<6:
        time.sleep(.25)

        enter = input("guess:   ")
        try:
            guess= int(enter)
            if guess<=100 and guess>=1:
                guessTaken= guessTaken+1

                if guessTaken<6:
                    if guess<number:
                        print("The number you have guesses is too low")

                    if guess>number:
                        print("The number you have guesses is too high")

                    if guess!=number:
                        time.sleep(.5)
                        print("Try again!")

                    if guess == number:
                        break

            if guess>100 and guess<1:
                print("stupid! it isn't in the range")
                time.sleep(.25)
                print("Enter the number in range")

        except:
            print("I don't think that" +enter+ "is a number. ")
    if guess == number:
        guessTaken = str(guessTaken)
        print("NICE JOB " +Name+ "You have guessed the right number, In {} guesses."(guessTaken))

    if guess !=number:
        print("You haven't guess the right number. The right number is "+str(number))

playagain =  "yes"

while playagain == "yes" or playagain== "y" or playagain=="YES":
    intro()
    pick()
    print("do you want to play again?")
    playagain= input()





        













