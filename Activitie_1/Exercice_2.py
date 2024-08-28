xa = int(input("Veuillez entrez l'abscisse du premier point: "))
ya = int(input("Veuillez entrez l'ordonnée du premier point: "))
xb = int(input("Veuillez entrez l'abscisse du deuxieme point: "))
yb = int(input("Veuillez entrez l'ordonnée du deuxieme point: "))

dist = ((xa-xb)**2+(ya-yb)**2)**1/2
print("\nLa distance entre ces deux points est:",dist)
