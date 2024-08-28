while True:
    sexe = input("Veuillez entrez votre sexe (M = masculin/F = feminin): ")
    try :
        taille = int(input("Veuillez entrez votre taille(cm): "))
        poids = int(input("Veuillez entrez votre poids(kg): "))
    except:
        print("Veuillez entrez des valeurs correctes!")
        print("-" * 50)
        continue

    if taille <= 0 or poids <= 0:
        print("Veuillez entrez des valeurs correctes!")
        print("-" * 50)
        continue

    if sexe.upper() == 'M':
        PI = taille - 100 -((taille-150)/4)
    elif sexe.upper() == 'F':
        PI = taille - 100 -((taille-120)/4)
    else:
        print("Veuillez entrez un sexe valide!")
        print("-"*50)
        continue
    BMI = poids/((taille*0.01)**2)
    print(f"Le poids ideal est: PI = {PI}")
    print(f"L'indicateur d'obésité est: BMI = {BMI:.2f}")
    break


