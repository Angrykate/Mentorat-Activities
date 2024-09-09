print("Ce programme vous permet d'effectuer des conversions de devices")
devises = ["Euro (€)", "Dollar ($)", "FCFA (₣)"]
index = 1
for i in range(len(devises)):
    for j in range(len(devises)):
        if i != j:
            print(f"{index} - {devises[i]} vers {devises[j]}")
            index += 1
print(f"{index} - Quitter")


def conversion(devise1, devise2, facteur):
    while True:
        valeur_initiale = input(
            f"Conversion {devise1} -> {devise2}. Donnez la valeur en {devise1} (Entrez un nombre negatif pour arreter): ")
        try:
            valeur_float = float(valeur_initiale)
        except ValueError:
            continue
        if valeur_float < 0:
            return
        valeur_convertie = round(valeur_float * facteur, 2)
        print(f"Résultat de la conversion: {valeur_float} {devise1} = {valeur_convertie} {devise2}")


while True:
    choix = input("Votre choix: ")
    if choix == str(index):
        print("A bientôt")
        break
    if not choix.isdigit() or int(choix) not in range(1,index):
        print("Veuillez entrez une valeur correcte!")
        continue
    print("-" * 50)
    match int(choix):
        case 1:
            conversion("Euro (€)", "Dollar ($)", 1.11)
        case 2:
            conversion("Euro (€)", "FCFA (₣)", 655.96)
        case 3:
            conversion("Dollar ($)", "Euro (€)", 0.90)
        case 4:
            conversion("Dollar ($)", "FCFA (₣)", 591.65)
        case 5:
            conversion("FCFA (₣)", "Euro (€)", 0.0015)
        case 6:
            conversion("FCFA (₣)", "Dollar ($)", 0.0016)
