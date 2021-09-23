import random

#liste de choix possibles
liste = ["rock", "paper", "scissors"]

#si le joueur veut jouer il répond yes
answer = "yes"
while answer == "yes":
    #choix du joueur
    user_choice = input("rock,paper,scissors ?")
    #choix de l'ordinateur
    prog = random.choice(liste)
    print("computer's choice :", prog)
    
    if ordi == "rock" :
        if user_choice == "paper" :
            print("you won") #gagné
        elif user_choice == "scissors" :
            print("you lost") #perdu
        else :
            answer = input("play again ?") #reponse du joueur
            
    if prog == "paper" :
        if user_choice == "scissors" :
            print("you won")
        elif user_choice == "rock" :
            print("you lost")
        else :
            answer = input("play again ?")
            
    if prog == "scissors" :
        if user_choice == "rock" :
            print("you won")
        elif user_choice == "paper" :
            print("you lost")
        else :
            answer = input("play again ?")
