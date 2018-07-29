"""--- The Second Game--- """
import random

secret = random.randint(1,10)
guess = -1

while guess != secret:
    temp = input("Please input a number to compare corrected number:")
    guess = int(temp)
    if guess == secret:
        print("This is corrected number!!!")
        print("But no award")
    else:
        if guess > secret:
            print("This number is larger than corrected number")
        else:
            print("This number is smaller than corrected number")
 #           temp = input("Please input a number to compare corrected number:")
 #           guess = int(temp)


print("Game over!!!")
