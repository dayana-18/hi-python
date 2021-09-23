from random import *

number = randint(1,50)

#reponse du joueur
answer = "y"
while answer == "y":
    #l'utilisateur a 15 chances pour trouver le nombre
    for i in range(0, 15):
        user_choice = int(input('choose a number between 1 and 50 :')) #choix du joueur
        if number > user_choice :
            print("the number is bigger!") #le nombre est plus grand
        if number < user_choice :
            print("the number is smaller!") #le nombre est plus petit
        if i >= 14 :
            print("you lost") #perdu
        if number == user_choice :
            print("you won") #gagné
            break
    print("the number was", number)
    answer = input('play again ? write y') #reponse du joueur
