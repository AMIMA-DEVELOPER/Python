import random

def roll_dice():
    """Generates a random number between 1 and 6."""
    return random.randint(1, 6)

def main():
    """Runs the dice rolling simulator."""
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        user_input = input("Press Enter to roll the dice or 'q' to quit: ").strip()
        if user_input == 'q':
            print("Goodbye!")
            break
        elif user_input == '':
            die_value = roll_dice()
            print(f"You rolled a {die_value}")
        else:
            print("Invalid input. Press Enter to roll or 'q' to quit.")

if __name__ == "__main__":
    main()
