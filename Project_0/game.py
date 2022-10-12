import numpy as np

number = np.random.randint(0, 101) 
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 0 to 100: 5"))

    if predict_number > number:
        print("Number must be less!")

    elif predict_number < number:
        print("Number must be greater!")

    else:
        print(f"You guessed the number in {count} attempts! This number is {number}")
        break