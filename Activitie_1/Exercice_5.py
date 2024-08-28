import os
import numpy
from random import randint

print("***Jeu de devinette (partie finale)***")
print()
dic = {'game':{'fac':[] , 'moy':[] , 'dif':[]},'score':{'fac':[] , 'moy':[] , 'dif':[]}} #stocker les resultats et scores


def get_the_number(bmax):
    global win,attempt
    win = False
    nbr_essai = 15
    number = randint(0, bmax)
    print(f"Trouve le nombre se situant entre 0 et {bmax}")
    while nbr_essai>0:
        print("Il te reste " + str(nbr_essai) + " essai" + ("s" if nbr_essai > 1 else ""))
        user_choice = input("Devine le nombre: ")
        if not user_choice.isdigit():
            print("Veuillez entrez un nombre  valide!")
            continue
        nbr_essai -= 1
        attempt = 15-nbr_essai
        if int(user_choice) > number:
            print("Le nombre mystère est plus petit que " + user_choice)
        elif int(user_choice) < number:
            print("Le nombre mystère est plus grand que " + user_choice)
        else:
            if attempt <= 3:
                print("\n* Super Voyant *\nLe nombre mystère était bien",number)
                print("Tu l'as eu en "+str(attempt)+" essais")
                win = True
                break
            elif attempt <= 6:
                print("\n* Sage Voyant *\nLe nombre mystère était bien",number)
                print("Tu l'as eu en " + str(attempt) + " essais")
                win = True
                break

            elif attempt <= 9:
                print("\n* Apprenti Voyant *\nLe nombre mystère était bien",number)
                print("Tu l'as eu en " + str(attempt) + " essais")
                win = True
                break

            else:
                print("\n*Pusilamine*\nLe nombre mystère était bien",number)
                print("Tu l'as eu en " + str(attempt) + " essais")
                win = True
                break
    else:
        print("Dommage! Le nombre mystère était " + str(number))


def game(bmax,dif):
    get_the_number(bmax)
    if win:
        dic['game'][dif].append(1)
        dic['score'][dif].append(attempt)
    else:
        dic['game'][dif].append(0)


def main():
    while True:
        print("""    \t1. Facile (0 -100) 
        2. Moyen (0 – 500) 
        3. Difficile (0 -1000)""")
        try:
            level = int(input("Veuillez sélectionner la difficulté: "))
        except ValueError:
            print("Veuillez entrer un nombre valide!")
            continue
        print("-" * 50)

        #selection de la difficulté
        match level:
            case 1:
                game(100,'fac')
            case 2:
                game(500,'moy')
            case 3:
                game(1000,'dif')
            case _:
                print("Veuillez entrez un nombre valide!")
                continue
        n = input("Voulez vous continuez? (o = oui): ")
        if n.lower() != 'o':
            break
        else:
            print("-" * 50)
            
            
def historique():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour Mac et Linux (os.name est 'posix')
        os.system('clear')
        
    print("\t\t-HISTORIQUE-")
    nbr_partie_fac =len(dic['game']['fac'])
    nbr_partie_moy =len(dic['game']['moy'])
    nbr_partie_dif =len(dic['game']['dif'])
    nbr_partie = nbr_partie_fac + nbr_partie_moy + nbr_partie_dif

    nbr_vic_fac = dic['game']['fac'].count(1)
    nbr_vic_moy = dic['game']['moy'].count(1)
    nbr_vic_dif = dic['game']['dif'].count(1)
    nbr_vic = nbr_vic_fac + nbr_vic_moy + nbr_vic_dif

    nbr_def_fac = dic['game']['fac'].count(0)
    nbr_def_moy = dic['game']['moy'].count(0)
    nbr_def_dif = dic['game']['dif'].count(0)
    nbr_def = nbr_def_fac + nbr_def_moy + nbr_def_dif

    print(f"*Nombre total de partie = {nbr_partie}")
    print()
    print(f"\t-Partie en difficulté facile = {nbr_partie_fac}")
    print(f"\t-Partie en difficulté moyenne = {nbr_partie_moy}")
    print(f"\t-Partie en difficulté difficile = {nbr_partie_dif}")
    print()
    print(f"*Nombre de victoire = {nbr_vic}")
    print()

    print(f"\t-Victoire en difficulté facile = {nbr_vic_fac}")
    for i in range(nbr_vic_fac):
        print(f"\t\t-{str(i + 1) + 'ere' if i == 0 else str(i + 1) + 'eme'} partie: victoire en {dic['score']['fac'][i]} tentatives")
    print(f"\t-Victoire en difficulté moyenne = {nbr_vic_moy}")
    for i in range(nbr_vic_moy):
        print(f"\t\t-{str(i + 1) + 'ere' if i == 0 else str(i + 1) + 'eme'} partie: victoire en {dic['score']['moy'][i]} tentatives")
    print(f"\t-Victoire en difficulté difficile = {nbr_vic_dif}")
    for i in range(nbr_vic_dif):
        print(f"\t\t-{str(i + 1) + 'ere' if i == 0 else str(i + 1) + 'eme'} partie: victoire en {dic['score']['dif'][i]} tentatives")
    print()

    print(f"*Nombre de defaite = {nbr_def}")
    print()
    print(f"\t-Defaite en difficulté facile = {nbr_def_fac}")
    print(f"\t-Defaite en difficulté moyenne = {nbr_def_moy}")
    print(f"\t-Defaite en difficulté difficile = {nbr_def_dif}")
    print("-" * 50)

    # Ecart type
    all_attemp = dic['score']['fac'] + dic['score']['moy'] + dic['score']['dif']
    print(f"Ecart type = {numpy.std(all_attemp) if len(all_attemp)>0 else 0}")

    # Moyenne olympique
    if len(all_attemp) >2:
        all_attemp.remove(max(all_attemp))
        all_attemp.remove(min(all_attemp))
    print(f"Moyenne olympique = {numpy.mean(all_attemp) if len(all_attemp)>0 else 0}")


main()
historique()
