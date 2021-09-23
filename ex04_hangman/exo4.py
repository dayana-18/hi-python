import random

#choisit un mot au hasard du fichier words.py
words = open('words.py').read().strip().split('", "')
word = random.choice(words)
print(word)

#l'utilisateur a 12 chances pour trouver le mot
for i in range(0, 12):
    user_choice = input('letter :')
    #parcours du mot
    for letter in word :
        if user_choice == letter :
            print(user_choice) #montre la ou les positions de la lettre
        if user_choice != letter : #si la lettre n'est pas dans le mot
            print("_") #les lettres manquantes
            print("the letter is not here")
    if user_choice == word : #s'il devine le mot
        print(word)
        print("you won")
