import random

cpu_number = random.randint(1,100)
attempts = 0
print("Guess the Computer's number from 1 to 100?")

while True:
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