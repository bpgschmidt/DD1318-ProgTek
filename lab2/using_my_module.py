import my_module

# Uppgift 1 (givet)

y = 222
x = 111
x_list = [111, 222, 333, 444]
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
my_module.scope_testing_function(x, x_list)
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2 (att skrivas)

print(my_module.my_function(15))

# Uppgift 3 (att skrivas)

print(my_module.roll_dice(3))

# Uppgift 4 (att skrivas)

listan = [4, 2, 1, 6, 4, 10, 111, 0, 203]
print(my_module.my_sort_list(listan))

# Uppgift 5 (att skrivas)

print(my_module.bandit_language("fint"))

# Uppgift 6 (givet)

animals = {'tiger': ['claws', 'sharp teeth', 'four legs', 'stripes'],
           'elephant': ['trunk', 'four legs', 'big ears', 'gray skin'],
           'human': ['two legs', 'funny looking ears', 'a sense of humor']
           }


# Uppgift 6 (att skrivas)

def make_bandit_dictionary(animals):
    new_dictionary = {}
    animals.values()
    animals.keys()
    for key, value in animals.items():
        animal_list = []
        for i in value:
            animal_list.append(my_module.bandit_language(i))
        new_dictionary[key] = animal_list
    return new_dictionary


print(make_bandit_dictionary(animals))
"""
for n in range(len(listan)):
    # for each element in the list in range n-1:
    for m in range(n + 1, len(listan)):
        # if the element before is larger, change the numbers
        print(listan[n])
        print(listan[m])
        if listan[n] > listan[m]:
            listan[n], listan[m] = listan[m], listan[n]
"""