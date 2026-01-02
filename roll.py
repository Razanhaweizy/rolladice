import random

terminate = False
dice_counter = 0

while not terminate:
    if dice_counter == 50:
        print("Wow, you're locked in... you have officially rolled 50 times")

    user_input = input("Roll the dice? Type c to view amount of dice rolled ").lower()

    if user_input == "y":
        dices = int(input("How many dice to roll? "))
        rolls = []
        res = ""
        for i in range(dices):
            rand_roll = random.randint(1, 6)
            rolls.append(str(rand_roll))
            dice_counter += 1
        res.join(rolls)
        print(f'({", ".join(rolls)})')
    elif user_input == "n":
        print("Thanks for playing!")
        terminate = True
        continue
    elif user_input == "c":
        print(f"You have rolled {dice_counter} dices >_<")
        continue
    else:
        print("Invalid choice :P")
        continue



