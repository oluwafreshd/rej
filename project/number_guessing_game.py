import random
secret_number = random.randint(0, 100)
guess = int(input("guess a number: "))

guessCount = 0
guessLimit = 3
while secret_number == guess:  #
    guessCount += 1
    print("correct")
else:
    print(f"wrong! The correct answer is {secret_number} Try again")
