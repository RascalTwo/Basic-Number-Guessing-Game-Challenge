import random

minmax = [1, 100]

while True:
    print "Choose A Action:"
    print "1. Play"
    print "2. Change Minimum & Maximum"
    print "3. Exit"
    choice = raw_input("")
    if choice.isdigit():
        if choice == "1":
            attempts = 1
            number = random.randint(minmax[0], minmax[1])
            while True:
                guess = raw_input("Guess (" + str(minmax[0]) + " - " + str(minmax[1]) + "): ")
                if guess.isdigit():
                    guess = int(guess)
                    if guess == number:
                        print "Correct!"
                        print "It Only Took You", attempts, "Attempts!" if attempts > 1 else "Attempt!"
                        break
                    elif guess > number:
                        print "That Guess Is Too High!"
                    elif guess < number:
                        print "That Guess Is Too Low!"
                else:
                    print "That's Not A Number!"
                attempts += 1
        elif choice == "2":
            getting_min_max = True
            while getting_min_max:
                minimum = raw_input("Minimum: ")
                if minimum.isdigit():
                    minmax[0] = int(minimum)
                    while True:
                        maximum = raw_input("Maximum: ")
                        if maximum.isdigit():
                            maximum = int(maximum)
                            if maximum > minmax[0]:
                                minmax[1] = maximum
                                getting_min_max = False
                                break
                            else:
                                print "Maximum Given Is Lower Then The Current Minimum(", minimum, ")"
                        else:
                            print "Not A Number"
                else:
                    print "Not A Number"
        elif choice == "3":
            print "Goodbye!"
            break
        else:
            print "Invalid Option!"
    else:
        print "Not A Number"
