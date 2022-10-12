# Guess the number game

import numpy as np

number = np.random.randint(1, 101) 
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))

    if predict_number > number:
        print("Number must be less!")

    elif predict_number < number:
        print("Number must be greater!")

    else:
        print(f"You guessed it with {count} attempts! This number is {number}")
        break