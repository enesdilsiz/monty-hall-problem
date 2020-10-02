# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 12:57:46 2020

@author: enesd
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
Yarışmamıza hoş geldiniz. 0, 1 ve 2 numaralı 3 tane kapımız bulunmaktadır.
Kapıların 2 tanesinin arkasında keçi, 1 tanesinin arkasında araba bulunmaktadır.
Öncelikle bu 3 kapı arasından birini seçmeniz gerekmektedir. Daha seçtiğiniz
kapı haricindeki 2 kapıdan arkasında keçi olan kapı açılıp kararınızı 
değiştirmek isteyip istemediğiniz sorulacaktır. Seçiminize göre en son
seçtiğiniz kapının arkasındaki ödül sizin olacaktır. Başarılar dilerim. :)
      """)

#X = ["goat","goat","car"]
#random.shuffle(X)

#inp = input("Please enter the one you want to choose from doors 0, 1 and 2:  ")
#inp= int(inp) 

#inp = random.randint(0,2)

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
#            print("\n" + str(i) + " has a goat behind it.")
#            yesno = input("\nDo you want to change your door?(yes/no)  ")
            yesno = random.choice(['yes', 'no']) 
            a=i
            
            if yesno == "yes":
                new = 3-inp-a
                if X[new] == "goat":
#                    print("\nYou changed your door to " + str(new) + " and win a goat")
                    changed_not_win += 1
                    break
                elif X[new] == "car":
#                    print("\nYou changed your door to " + str(new) + " and win a car")
                    changed_win += 1
                    break
            elif yesno == "no":
                if X[inp] == "goat":
#                    print("\nYou keep your door and win a goat")
                    not_changed_not_win += 1
                    break
                elif X[inp] == "car":
#                    print("\nYou keep your door and win a car")
                    not_changed_win += 1
                    break
#print("\nThe gates were like: ")
#print(X)
changed_win_ratio = changed_win/(changed_win + changed_not_win)
not_changed_win_ratio = not_changed_win/(not_changed_win + not_changed_not_win)

print("Karar değiştirildiğindeki başarı oranı: ", changed_win_ratio)
print("Karar değiştirilmediğindeki başarı oranı: ", not_changed_win_ratio)
