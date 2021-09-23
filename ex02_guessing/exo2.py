from random import *

number = randint(1,50)

#l'utilisateur a 10 chances pour trouver le nombre
for i in range(0, 20):
    user_choice = int(input('choose a number :')) #choix du joueur
    if number > user_choice :
        print("the number is bigger!") #le nombre est plus grand
    if number < user_choice :
        print("the number is smaller!") #le nombre est plus petit
    if number == user_choice :
        print("you won") #gagné
        break
print("the number was", number)
