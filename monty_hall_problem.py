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
while True:
    
    X = ["goat","goat","car"]
    
    random.shuffle(X)
    
    cond1 = False
    cond2 = False
    cond3 = False
    
    while cond1 == False:
        inp = input("Please enter the one you want to choose from doors 1, 2 and 3:  ")
        if inp == '1' or inp == '2' or inp == '3':
            cond1 = True
        else:
            print("\nInvalid door number, please choose a valid door number 1, 2, 3")
    

    inp = int(inp) 
    inp -= 1
    
    
    for i in range(3):
        
        if X[i] == "goat" and i != inp:
            print("\nDoor " + str(i+1) + " has a goat behind it.")
            
            while cond2 == False:
                yesno = input("\nWould you like to change your door with the other door?(Yes: y / No: n)  ")
                if yesno == 'y' or yesno == 'n':
                    cond2 = True
                else:
                    print("\nInvalid syntax, please type y for Yes and n for No")
            
            a=i
            
            if yesno == "y":
                new = 3-inp-a
                if X[new] == "goat":
                    print("\nYou change your door from " + str(inp+1) + " to " + str(new+1) + " and win a GOAT.")
                    break
                elif X[new] == "car":
                    print("\nYou change your door from " + str(inp+1) + " to " + str(new+1) + " and win a CAR!")
                    break
            elif yesno == "n":
                if X[inp] == "goat":
                    print("\nYou keep your door and win a GOAT.")
                    break
                elif X[inp] == "car":
                    print("\nYou keep your door and win a CAR!")
                    break
            else:
                print("\nYou made an invalid choice. Please just type 'y' or 'n'.")
                continue
    
    print("\nThe gates were like 1: %s, 2: %s, 3: %s " %(X[0],X[1],X[2]))
    
    while cond3 == False:
        c = input("\nWould you like to play another round or quit?(Play: p / Quit: q)  ")
        if c == 'p' or c == 'q':
            cond3 = True
        else:
            print("\nInvalid syntax, please type p for Play and q for Quit")
    
    if c == "q":
        break
