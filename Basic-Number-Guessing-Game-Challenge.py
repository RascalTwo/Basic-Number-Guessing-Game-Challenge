import random

number = str(random.randint(1, 100))
while True:
    if raw_input("Guess (1 - 100): ") == number:
        print "Correct!"
        break
    else:
        print "Incorrect, Guess Again!"
