__author__ = 'Vinothini Pushparaja'
# for i in range(1, 20):
#     print("i is now {}".format(i))
#
# print("\n")
# number = "9,234,456,867,567,098,234"
# for i in range(0, len(number)):
#     print(number[i])

number = "9,234,456,867,567,098,234"
cleanedNumber = ""
for i in range(0, len(number)):
    if number[i] in "0123456789":
        #print(number[i], end='')
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The new number is {}".format(newNumber))