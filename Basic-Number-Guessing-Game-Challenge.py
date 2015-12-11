import random

attempts = 1
number = str(random.randint(1, 100))
while True:
    print number
    if raw_input("Guess (1 - 100): ") == number:
        print "Correct!"
        print "It Only Took You", attempts, "Attempts!" if attempts > 1 else "Attempt!"
        break
    else:
        print "Incorrect, Guess Again!"
        attempts += 1
