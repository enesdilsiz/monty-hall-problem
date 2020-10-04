"""
Monty Hall Problem Statistics - @author: enesdilsiz
"""
import random

print(
"""
  __  __             _           _    _       _ _   _____           _     _                
 |  \/  |           | |         | |  | |     | | | |  __ \         | |   | |               
 | \  / | ___  _ __ | |_ _   _  | |__| | __ _| | | | |__) | __ ___ | |__ | | ___ _ __ ___  
 | |\/| |/ _ \| '_ \| __| | | | |  __  |/ _` | | | |  ___/ '__/ _ \| '_ \| |/ _ \ '_ ` _ \ 
 | |  | | (_) | | | | |_| |_| | | |  | | (_| | | | | |   | | | (_) | |_) | |  __/ | | | | |
 |_|  |_|\___/|_| |_|\__|\__, | |_|  |_|\__,_|_|_| |_|   |_|  \___/|_.__/|_|\___|_| |_| |_|
                          __/ |                                                            
                         |___/                                                             
"""
)

print("""
      This program tests the Monty Hall Problem with number of iterations 
      and calculates the likelihood in different situations.
""")

changed_win=0
changed_not_win=0
not_changed_win=0
not_changed_not_win=0

for j in range(1000):
    X = ["goat","goat","car"]
    random.shuffle(X)
    inp = random.randint(0,2)
    
    for i in range(3):
        if X[i] == "goat" and i != inp:
            yesno = random.choice(['yes', 'no']) 
            a=i
            
            if yesno == "yes":
                new = 3-inp-a
                if X[new] == "goat":
                    changed_not_win += 1
                    break
                elif X[new] == "car":
                    changed_win += 1
                    break
            elif yesno == "no":
                if X[inp] == "goat":
                    not_changed_not_win += 1
                    break
                elif X[inp] == "car":
                    not_changed_win += 1
                    break

changed_win_ratio = changed_win/(changed_win + changed_not_win)
not_changed_win_ratio = not_changed_win/(not_changed_win + not_changed_not_win)

print("1000 iteration were made and the results are as follows: \n")
print("Success rate when the decision is     CHANGED: %", round(changed_win_ratio,2)*100)
print("Success rate when the decision is NOT CHANGED: %", round(not_changed_win_ratio,2)*100)
