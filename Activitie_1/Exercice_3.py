from random import randint


def get_the_number(bmax):
    number = randint(0, bmax)
    print(f"Trouve le nombre se situant entre 0 et {bmax}")
    user_choice = -1
    while int(user_choice)!=number:
        user_choice = input("Devine le nombre: ")
        if not user_choice.isdigit():
            print("Veuillez entrez un nombre  valide!")
            continue
        if int(user_choice) > number:
            print("Le nombre mystère est plus petit que " + user_choice)
        elif int(user_choice) < number:
            print("Le nombre mystère est plus grand que " + user_choice)
        else:
            print("Bravo! Le nombre mystère était bien " + str(number))


if __name__ == '__main__': # la condition vérifie si le script est exécuté directement et non importé
    print("***Jeu de devinette (1ere partie)***")
    print()
    x = int(input("Veuillez entrez la borne maximale du nombre: "))
    get_the_number(x)