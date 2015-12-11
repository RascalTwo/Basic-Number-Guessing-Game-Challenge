import random

print "Correct!" if raw_input("Guess (1 - 100): ") == str(random.randint(1, 100)) else "Incorrect!"
