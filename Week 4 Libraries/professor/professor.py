from random import randint
def main():
    #Prompt user for a level
    level = get_level()
    #Randomly generate ten math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer
    problems = 10
    #track score
    score=[]
    while problems != 0:
        x = generate_integer(level)
        y = generate_integer(level)
        #allow three tries in total for a problem
        tries = 3
        while tries != 0:
            #Prompt the user to solve each of ten problems
            answer = input(f"{x} + {y} =")
            #If an answer is not correct, output EEE and prompt user again
            if int(answer) != x+y:
                print("EEE")
                tries -= 1
                #if still not answered correctly output the correct answer
                if tries == 0:
                    print(f"{x} + {y} ={x+y}")
                    problems -= 1
            else:
                problems -= 1
                score.append(answer)
                break # Breaks out of the while tries loop
        # output the user’s score: the number of correct answers out of 10
        if problems == 0:
            print(f"Score: {len(score)}")
#prompt (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
            else:
                raise ValueError
        except:
            pass


#return a randomly generated non-negative integer with level digits
def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    else:
        return randint(100, 999)

if __name__ == "__main__":
    main()