from random import *

#rock = 0
#paper = 1
#scissors = 2

#liste = ["rock", "paper", "scissors"]
choix = int(input("play"))

#ordi = randint(0, len(liste) - 1)
ordi = randint(0, 2)
print("computer's choice :", ordi)
if ordi == 0 :
    if choix == 1 :
        print("you won")
    elif choix == 2 :
        print("you lost")
    else :
        print("play again")
if ordi == 1 :
    if choix == 2 :
        print("you won")
    elif choix == 0 :
        print("you lost")
    else :
        print("play again")
if ordi == 2 :
    if choix == 0 :
        print("you won")
    elif choix == 1 :
        print("you lost")
    else :
        print("play again")      
    
