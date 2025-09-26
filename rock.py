import random
print("welcome to rock papaer scissors game\n")
player_wins= 0
computer_wins=0
while True:
    player= input("Enter a choice(rock,papare,scissors):")
    choices=["rock","paper","scissors"]
    computer = random.choice(choices)
    print(f"\nYou chose {player}, computer chose{computer}.")

    if player == computer:
        print(f"Both players selected{player}. It is a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Rock beats scissoers you win!!")
            player_wins+=1

        else:
            print("Paper beats rock. You lose.")
            computer_wins+=1
    elif player == "paper":
        if computer == "rock":
           print("paper beats rock you win!!")
           player_wins+=1

        else:
             print("scissors cut paper you lose.")
             computer_wins+=1

    elif player == "scissors":
            if computer == "paper":
                 print("scissors cut paper you win!!")
            else:
                 print("rock beats scisor you lose!")
                 computer_wins+=1
print("You have" + str(player_wins)+"  wins")     
print("The computer has " +str(computer_wins)+"  wins")
repeat = input("\n play again??(yes/no): ")
if repeat.lower() != "yes":
     print("Thanks for playing")