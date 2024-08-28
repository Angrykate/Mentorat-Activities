x = input("Veuillez saisir le premier nombre: ")
y = input("Veuillez saisir le deuxieme nombre: ")
operateur = input("Veuillez entrez l'operateur ")

try:
    resultat = eval(x+operateur+y)# eval() evalue l'expression et l'execute comme un code python
except:
    print("Operateur non definie")
    exit()

print(f"{float(x):.2f} {operateur} {float(y):.2f} = {resultat:.2f}")

