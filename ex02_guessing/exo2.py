from random import *

number = randint(1,100)

choice = int(input("choisis un nombre"))

if number > choice :
    print("plus haut")
if number < choice :
    print("plus bas")
if number == choice :
    print("GG")
print(number)
