# Lab 1
# Trial 1

# print Kim
nice_name = 'Kim'
print(nice_name)

# print Kim 33 times
long_name = ''
for x in range(0, 33):
    long_name += nice_name
print(long_name)

# Trial 2
# input, raw input means that you don't have to write "" in the console. Fantastic.
username = raw_input('Vad heter du? ')
# output
for y in range(0, 39):
    print(username)

# Trial 3
inputName = ''
while inputName != 'Sauron':
    inputName = raw_input('Vad heter du? ')
    print('Tjena ' + inputName)

# Trial 5
import math
n = int(input("skriv ett tal n (ex: 10, 100, 1000): "))
tal = (math.pi * math.pi) / 6
piIsh = 0.0
for z in range(1, n + 1):  # type: float
    piIsh += 1.0/(z*z)
print(tal)
print(piIsh)
