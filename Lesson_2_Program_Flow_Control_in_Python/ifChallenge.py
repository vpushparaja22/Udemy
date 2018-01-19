__author__ = 'Vinothini Pushparaja'
# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 17 < age < 31:
    print("Hello {0}! Welcome to the holiday of the year.".format(name))
else:
    print("Sorry for the inconvenience. This holiday is only for people whose age is between 18 - 30.")