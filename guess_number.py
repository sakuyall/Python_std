# guess number code & random number-1/3/25----------------------------------------------
import random

counts = 3
answer = random.randint(0,10)

while counts > 0:

    temp = input("guess the number from 0 to 10:")
    guess = int(temp)

    if guess == answer:
        print("yeah,\nbut no treasure.")
        break
    else:
        if guess < answer:
            print("a little small")
        else:
            print("a little big")

    counts = counts - 1

    if counts != 0:
        print("please try again")
    else:
        print("all is over")
        print("the answer is:")
        print(answer)

# x = random.getstate()
# print(x)
# random.setstate(x)
    