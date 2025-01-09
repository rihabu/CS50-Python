import random

#Prompt the user for a level n,If the user does not input a positive integer, prompt again.
while True:
    try:
        level= int(input("Level: "))
        if level>0:
            break
    except:
        pass

#Randomly generates an integer between 1 and n , inclusive, using the random module.
random_int = random.randrange(0, level+1)

#Prompt the user to guess that integer. If the guess is not a positive integer, prompt the user again.
while True:
    try:
        guess = int(input("Guess: "))
        if guess<random_int:
            print("Too small!")
        elif guess>random_int:
            print("Too large!")
        else:
            print("Just right!")
            break
    except:
        pass