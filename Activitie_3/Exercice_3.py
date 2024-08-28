class Livre:
    def __init__(self, titre, auteur, isbn):
        self.__titre = titre
        self.__auteur = auteur
        self.__isbn = isbn
        self.__disponible = True

    def getDisponibilité(self):
        return self.__disponible

    def getTitre(self):
        return self.__titre

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
        else:
            print("Ce livre n'est pas disponible!")

    def retourner(self):
        self.__disponible = True


class Membre:
    def __init__(self, nom, id_membre):
        self.__nom = nom
        self.__id_membre = id_membre
        self.__livre_empruntes = []

    def getNom(self):
        return self.__nom

    def getLivreEmpruntes(self):
        return self.__livre_empruntes

    def getNom(self):
        return self.__nom

    def emprunter_livre(self, livre):
        if livre.getDisponibilité():
            livre.emprunter()
            self.__livre_empruntes.append(livre.getTitre())
            return True
        else:
            print(f"Le livre ({livre.getTitre()}) n'est pas disponible à l'emprunt!")

    def retourner_livre(self,livre):
        if livre.getDisponibilité():
            print(f"Le livre ({livre.getTitre()}) n'est pas emprunter!")
        else:
            livre.retourner()
            self.__livre_empruntes.remove(livre.getTitre())
            return True

class Bibliotheque:
    def __init__(self,nom,livres=[],membres=[]):
        self.__nom = nom
        self.__livres = livres
        self.__membres = membres

    def ajouter_livre(self,livre):
        if livre in self.__livres:
            print(f"le livre ({livre.getTitre()}) existe déjà dans notre bibliotheque!")
        else:
            self.__livres.append(livre)

    def inscrire_membre(self,membre):
        if membre in self.__membres:
            print(f"le membre ({membre.getNom()}) est déjà inscrit dans notre bibliotheque!")
        else:
            self.__membres.append(membre)

    def lister_livres_disponibles(self):
        D = False
        for livre in self.__livres:
            if livre.getDisponibilité():
                print(f"- {livre.getTitre()}")
                D = True
        if not self.__livres or not D:
            print("Aucun livre n'est disponible à l'emprunt!")

    def lister_livres_empruntes(self):
        D = False
        for livre in self.__livres:
            if not livre.getDisponibilité():
                print(f"- {livre.getTitre()}")
                D = True
        if not self.__livres or not D:
            print("Aucun livre d'emprunter!")



L1 = Livre("Harry_potter", "J.K rowling", 817571)
L2 = Livre("Game_of_Thrones", "George R.R. martin", 782123)
L3 = Livre("Hunger_Games", "Susanne Collins", 456803)

M1 = Membre("Joe",100)
M2 = Membre("Alex",99)

B = Bibliotheque("Sainte_Genevieve")

M1.emprunter_livre(L1)
M2.emprunter_livre(L2)

B.ajouter_livre(L1)
B.ajouter_livre(L2)
B.ajouter_livre(L3)

B.inscrire_membre(M1)
B.inscrire_membre(M2)
B.lister_livres_disponibles()

