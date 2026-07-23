import random

click = 0

while True:
    input("Press Enter to click: ")
    click += 1

    if click % 2 == 0:
        print("Rolling...")
        print("Dice:", random.randint(1, 6))
    else:
        print("Stopped")