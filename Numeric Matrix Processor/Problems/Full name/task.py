f1 = open('name.txt')
f2 = open('surname.txt')
f3 = open('full_name.txt', 'w')

name = f1.read()
surname = f2.read()

full_name = name + ' ' + surname

f3.write(full_name)

with open("name.txt") as f1:
    with open("surname.txt") as f2:
        with open("full_name", "w") as f3:
            f3.write(full_name)