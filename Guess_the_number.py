import random
r_number = random.randint(0,100)

tries = 0
guess = int(input("Guess the random number between 0 and 100: "))

while (guess != r_number):
    if (guess < r_number):
        guess = int(input("Higher: "))
        tries += 1
    elif (guess > r_number):
        guess = int(input("Lower: "))
        tries += 1

print (f"You won in {tries} tries")