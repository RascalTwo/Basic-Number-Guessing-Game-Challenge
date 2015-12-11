from random import randint

minmax = [1, 100]


def menu():
    while True:
        print "Choose An Action:"
        print "1. Play"
        print "2. Change Minimum And Maximum"
        print "3. Exit"

        choice = raw_input("")
        if is_int(choice):
            choice = to_int(choice)
            if 1 <= choice and choice <= 3:
                if choice == 1:
                    play()
                elif choice == 2:
                    config()
                elif choice == 3:
                    exit()
            else:
                print "Invalid Input. Expected A Number From 1 To 3."
        else:
            print "Invalid Input. Expected A Number."


def play():
    attempts = 1
    number = randint(minmax[0], minmax[1])
    while True:
        guess = raw_input("Guess (%s - %s): " % (minmax[0], minmax[1]))
        if is_int(guess):
            guess = to_int(guess)
            if minmax[0] <= guess and guess <= minmax[1]:
                if guess == number:
                    print "Correct!"
                    print "It Only Took You %s Attempt%s!" % (attempts, "s" if attempts > 1 else "")
                    menu()
                else:
                    print "Your Guess Is Too %s, Guess Again!" % ("High" if guess > number else "Low")
            else:
                print "Expected A Number From %s To %s!" % (minmax[0], minmax[1])
        else:
            print "Expected A Number."
        attempts += 1


def config():
    global minmax
    while True:
        minimum = raw_input("Minimum: ")
        if is_int(minimum):
            minmax[0] = to_int(minimum)
            while True:
                maximum = raw_input("Maximum: ")
                if is_int(maximum):
                    maximum = int(maximum)
                    if maximum > minmax[0]:
                        minmax[1] = maximum
                        menu()
                    else:
                        print "Maximum Given Is Lower Then The Current Minimum(%s)" % (minimum)
                else:
                    print "Expected A Number."
        else:
            print "Expected A Number."


def exit():
    print "Thanks For Playing!"


def is_int(string):
    return True if string.replace(" ", "").replace("-", "").isdigit() else False


def to_int(string):
    try:
        return int(string)
    except:
        raise ValueError("Could Not Parse %s Into A Integer" % string)


menu()
