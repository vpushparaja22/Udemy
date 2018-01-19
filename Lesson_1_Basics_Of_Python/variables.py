__author__ = 'Vinothini Pushparaja'

parrot = "Norwegian Blue"
print(parrot[0])
print(parrot[1])
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:2])
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])
num = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(num[0::3])
string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's" "probably" " pining")

print("Hello " *5)
print("Hello " *(5+4))
print("Hello " * 5 + "4")

today = "friday"

print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")
