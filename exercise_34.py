# Birthday JSON

import json
import time

def add_entry():
    name = input("Please enter the person's name:\n>>>")
    born = input("Please enter the person's birthday:\n>>>")
    bday[name] = born
    with open('info.json', 'w') as f:
        json.dump(bday, f)

def look_entry():
    search = input('Whose birthday you want to know?\n>>>')
    if search in bday:
        print("{}'s birthday is {}.".format(search, bday[search]))
    else:
        print("Sorry we don't have {}'s birthday in our Birthday Dictionary. Maybe you can add {} to our Birthday Dictionary.".format(search, search))

def show_entry():
    for k, v in bday.items():
        print(k)

if __name__ == '__main__':
    with open('info.json', 'r') as f:
        bday = json.load(f)
    print('Welcome to the Birthday Dictionary. We know the birthday of:')
    for k, v in bday.items():
        print(k)
    while True:
        want = int(input('\nWhat do you want to do?\n1) Add birthday\n2) Search birthday\n3) Show birthday\n4) Quit\n>>>'))
        if want == 1:
            add_entry()
        elif want == 2:
            look_entry()
        elif want == 3:
            show_entry()
        elif want == 4:
            break
