from Exercice_3 import get_the_number
print("***Jeu de devinette (2eme partie)***")
print()
print("""1. Facile (0 -100) 
2. Moyen (0 – 500) 
3. Difficile (0 -1000)""")
level = int(input("Veuillez sélectionner la difficulté: "))
print("-"*50)
match level:
    case 1:
        get_the_number(100)
    case 2:
        get_the_number(500)
    case 3:
        get_the_number(1000)
    case _:
        print("Veuillez entrez un nombre valide!")
