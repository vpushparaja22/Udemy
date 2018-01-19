__author__ = 'Vinothini Pushparaja'

# age = int(input("How old are you?"))

# ways of writing a range of values
#if (age >= 16) and (age <= 65):
#if 16 <= age <= 65:
# if 15 < age < 66:
#     print("Have a good day at work.")

# if (age < 16) or (age > 65):
#     print("Enjoy your free time.")
# else:
#     print("Have a good day at work.")
#
# x = "false"
# if x:
#     print("x is true")
# else:
#     print("x is false")
#
# x = input("Enter some text: ")
# if x:
#     print("You have entered '{}'!".format(x))
# else:
#     print("You did not enter anything")

# print(not True)
# print(not False)

# if not(age < 18):
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years.".format(18-age))

name = "Kaggle competition"

letter = input("Enter a character: ")
# if letter in name:
#     print("Give me an {0} Bob".format(letter))
# else:
#     print("I don't need that letter")

if letter not in name:
    print("I don't need that letter")
else:
    print("Give me an {0} Bob".format(letter))