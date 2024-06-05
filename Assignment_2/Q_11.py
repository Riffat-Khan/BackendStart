# Write a program that simulates coin tossing. For each toss of the coin, the program should
# print Heads or Tails. Let the program toss the coin 100 times, and count the number of times
# each side of the coin appears and then print the results. The program should call a separate
# function flip that takes no arguments and returns 0 for tails and 1 for heads. Note: To get
# random 1 or 0 you can import a random module and then use random.randint(0,1)

import random

def flip():
    if random.randint(0,1) == 0 : return "tail"
    elif random.randint(0,1) == 1 : return "head"

def coinTossing ():
    start = 1
    headCount = tailCount = 0
    while start <=100:
        if flip() == "tail": tailCount +=1
        elif flip() == "head": headCount +=1
        start +=1

    print("Total no. of head count:" , headCount)
    print("Total no. of tail count:" , tailCount)


coinTossing()
    