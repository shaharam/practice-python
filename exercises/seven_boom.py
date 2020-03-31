# The function gets an int and print all the numbers from 1 to int
# if the num divisible by 7 or 11 using modulo print "boom"/"trach"

# Declare constants for later change
BOOM = 7
TRACH = 11


def seven_boom(x):
    for i in range(1, x+1):     # Run from 1 to x (inclusive)
        if i % BOOM == 0:
            print "Boom"
        elif i % TRACH == 0:
            print "Trach"
        else:
            print i


seven_boom(23)  # Testing
