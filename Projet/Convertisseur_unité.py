print("Ce programme vous permet d'effectuer des conversions d'unités")
Unité = ["Cm", "Pouces", "Celsius(°C)", "Fahrenheit(°F)", "Joules(J)", "Calories(cal)"]
index = 1
for i in range(len(Unité)):
    if i % 2 != 0:
        print(f"{index} - {Unité[i]} vers {Unité[i - 1]}")
        index += 1
    else:
        print(f"{index} - {Unité[i]} vers {Unité[i + 1]}")
        index += 1
print(f"{index} - Quitter")


def conversion(unit1, unit2, facteur, facteur_op=0.0):
    while True:
        valeur_initiale = input(
            f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (Entrez un nombre negatif pour arreter): ")
        try:
            valeur_float = float(valeur_initiale)
        except ValueError:
            continue
        if valeur_float < 0:
            return
        valeur_convertie = round((valeur_float * facteur) + facteur_op, 2)
        print(f"Résultat de la conversion: {valeur_float} {unit1} = {valeur_convertie} {unit2}")


while True:
    choix = input("Votre choix: ")
    if choix == str(index):
        print("A bientôt")
        break
    if not choix.isdigit() or int(choix) not in range(1, len(Unité) + 1):
        print("Veuillez entrez une valeur correcte!")
        continue
    print("-" * 50)
    match int(choix):
        case 1:
            conversion("cm", "inch", 0.394)
        case 2:
            conversion("inch", "cm", 2.54)
        case 3:
            conversion("Celsius", "Fahrenheit", 1.8, 32)
        case 4:
            conversion("Fahrenheit", "Celsius", 5 / 9, -32 * 5 / 9)
        case 5:
            conversion("Joules", "Calories", 0.24)
        case 6:
            conversion("Calories", "Joules", 4.184)
