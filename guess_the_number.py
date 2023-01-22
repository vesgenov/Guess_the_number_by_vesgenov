import random

cpu_number = random.randint(1,100)
attempts = 0
question = "Guess the Computer's number from 1 to 100?"
print("Choose difficulty:")
print("     Easy (unlimited attempts to guess the number) press 1")
print("     Novice (15 attempts to guess the number) press 2")
print("     Medium (10 attempts to guess the number) press 3")
print("     Hard (5 attempts to guess the number) press 4")
difficulty = int(input())


while True:

    if difficulty == 2:
        if attempts == 15:
            print("Game over")
            print("Play again? y/n")
            choice = input()
            if choice == "y":
                attempts = 0
                cpu_number = random.randint(1,100)
                continue
            elif choice == "n":
                break
    elif difficulty == 3:
        if attempts == 10:
            print("Game over")
            print("Play again? y/n")
            choice = input()
            if choice == "y":
                attempts = 0
                cpu_number = random.randint(1, 100)
                continue
            elif choice == "n":
                break
    elif difficulty == 4:
        if attempts == 5:
            print("Game over")
            print("Play again? y/n")
            choice = input()
            if choice == "y":
                attempts = 0
                cpu_number = random.randint(1, 100)
                continue
            elif choice == "n":
                break

    print(question)
    if difficulty == 1:
        print("Remaining attempts - ∞")
    elif difficulty == 2:
        print(f"Remaining attempts - {15 - attempts}")
    elif difficulty == 3:
        print(f"Remaining attempts - {10 - attempts}")
    elif difficulty == 4:
        print(f"Remaining attempts - {5 - attempts}")

    my_num = input()
    if not my_num.isdigit():
        print("Wrong input! Try again!")
        continue
    else:
        my_num = int(my_num)
    attempts += 1
    if my_num == cpu_number:
        print(f"You win! The number is {cpu_number}.")
        print(f"You tried {attempts} times.")
        break
    else:
        if my_num > cpu_number:
            print("Too high!")
            continue
        if my_num < cpu_number:
            print("Too low!")
            continue
