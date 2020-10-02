# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:04:50 2020

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

X = ["goat","goat","car"]
random.shuffle(X)

inp = input("Please enter the one you want to choose from doors 0, 1 and 2:  ")
inp= int(inp) 


for i in range(3):
    if X[i] == "goat" and i != inp:
        print("\n" + str(i) + " has a goat behind it.")
        yesno = input("\nDo you want to change your door?(yes/no)  ")
        a=i
        
        if yesno == "yes":
            new = 3-inp-a
            if X[new] == "goat":
                print("\nYou changed your door to " + str(new) + " and win a goat")
                break
            elif X[new] == "car":
                print("\nYou changed your door to " + str(new) + " and win a car")
                break
        elif yesno == "no":
            if X[inp] == "goat":
                print("\nYou keep your door and win a goat")
                break
            elif X[inp] == "car":
                print("\nYou keep your door and win a car")
                break
print("\nThe gates were like: ")
print(X)
