"""
Monty Hall Problem Game - @author: enesdilsiz
"""
import random

print("""
  __  __             _           _    _       _ _   _____           _     _                
 |  \/  |           | |         | |  | |     | | | |  __ \         | |   | |               
 | \  / | ___  _ __ | |_ _   _  | |__| | __ _| | | | |__) | __ ___ | |__ | | ___ _ __ ___  
 | |\/| |/ _ \| '_ \| __| | | | |  __  |/ _` | | | |  ___/ '__/ _ \| '_ \| |/ _ \ '_ ` _ \ 
 | |  | | (_) | | | | |_| |_| | | |  | | (_| | | | | |   | | | (_) | |_) | |  __/ | | | | |
 |_|  |_|\___/|_| |_|\__|\__, | |_|  |_|\__,_|_|_| |_|   |_|  \___/|_.__/|_|\___|_| |_| |_|
                          __/ |                                                            
                         |___/                                                             
""")

print("""
      Welcome to the contest. We have 3 doors numbered 0, 1 and 2. 
      There are goats behind 2 of the doors and a car behind 1 of them.
      First of all, you have to choose one of these 3 doors.
      You will be asked if you want to change your decision 
      by opening the door with a goat behind it from 2 doors 
      other than the one you have selected. The prize behind 
      the last door you choose will be yours. Good luck. :)
""")

X = ["goat","goat","car"]

random.shuffle(X)

inp = input("Please enter the one you want to choose from doors 0, 1 and 2:  ")

inp= int(inp) 


for i in range(3):
    if X[i] == "goat" and i != inp:
        print("\nDoor " + str(i) + " has a goat behind it.")
        yesno = input("\nWould you like to change your door with the other door?(yes/no)  ")
        a=i
        
        if yesno == "yes":
            new = 3-inp-a
            if X[new] == "goat":
                print("\nYou change your door from " + str(inp) + " to " + str(new) + " and win a GOAT.")
                break
            elif X[new] == "car":
                print("\nYou change your door from " + str(inp) + " to " + str(new) + " and win a CAR!")
                break
        elif yesno == "no":
            if X[inp] == "goat":
                print("\nYou keep your door and win a GOAT.")
                break
            elif X[inp] == "car":
                print("\nYou keep your door and win a CAR!")
                break

print("\nThe gates were like 0: %s, 1: %s, 2: %s " %(X[0],X[1],X[2]))
