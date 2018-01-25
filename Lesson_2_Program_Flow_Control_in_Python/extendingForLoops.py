__author__ = 'Vinothini Pushparaja'

number = "9,987,354,876,234,983,095,675"
cleanedNumber = ""

for char in number:
    if char in "0123456789":
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["non pinin", "no more", "a stiff", "bereft of life"]:
    print("The parrot is" + state)
    # Can also be written as
    # print("The parrot is {}".format(state))

# to skip a step add 3rd parameter in range() function
for i in range(0, 100, 5):
    print("i is {}".format(i))

# Nested for loops
for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(i, j, i*j))
    print("=================")