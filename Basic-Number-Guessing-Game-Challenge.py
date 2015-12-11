import random

attempts = 1
number = random.randint(1, 100)
while True:
    guess = raw_input("Guess (1 - 100): ")
    if guess.isdigit():
        guess = int(guess)
        if 1 <= guess and guess <= 100:
            if guess == number:
                print "Correct!"
                print "It Only Took You", attempts, "Attempts!" if attempts > 1 else "Attempt!"
                break
            elif guess > number:
                print "That Guess Is Too High!"
            elif guess < number:
                print "That Guess Is Too Low!"
        else:
            print "Guesses Must Be Between 1 And 100!"
    else:
        print "That's Not A Number!"
    attempts += 1
