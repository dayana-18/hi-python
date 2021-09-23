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
            print(user_choice)
        if user_choice != letter :
            print("_")
            print("the letter is not here")
    if user_choice == word :
        print(word)
        print("you won")
