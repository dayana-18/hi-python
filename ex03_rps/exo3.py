import random

#liste de choix possibles
liste = ["rock", "paper", "scissors"]

#si le joueur veut jouer il répond y
answer = "y"
while answer == "y":
    #choix du joueur
    user_choice = input("rock,paper,scissors ?")

    #verifie si le joueur a mis la réponse correcte
    if user_choice in liste :
        #choix de l'ordinateur
        prog = random.choice(liste)
        print("computer's choice :", prog)

        if prog == "rock" :
            if user_choice == "paper" :
                print("you won") #gagné
            elif user_choice == "scissors" :
                print("you lost") #perdu
                
        if prog == "paper" :
            if user_choice == "scissors" :
                print("you won")
            elif user_choice == "rock" :
                print("you lost")
                
        if prog == "scissors" :
            if user_choice == "rock" :
                print("you won")
            elif user_choice == "paper" :
                print("you lost")

    else :
        print("not the correct answer")
    
    #demande si le joueur veut jouer
    answer = input("play again ? write y")
