class Employe:
    valSal = 100

    def __init__(self, nom, matricule, indSal):
        self.nom = nom
        self.matricule = matricule
        self.indSal = indSal

    def afficherInfos(self):
        return f"Matricule: N°{self.matricule}\nNom: {self.nom}"

    def salaire(self):
        return f"Salaire du matricule N°{self.matricule}: {self.indSal * self.valSal}$"


class Responsable(Employe):
    def __init__(self, nom, matricule, indSal):
        super().__init__(nom, matricule, indSal)
        self.inf_Hierarchique = []

    def ajouter_inf(self, employe):
        self.inf_Hierarchique.append(employe)

    def afficher_inférieur(self):
        print(f"Inférieurs directs de {self.nom}: ")
        for i in self.inf_Hierarchique:
            print(i.nom)


class Commercial(Employe):
    def __init__(self, nom, matricule, indSal, ventes=0):
        super().__init__(nom, matricule, indSal)
        self.ventes = ventes

    def mis_a_jour_ventes(self, nvVentes):
        self.ventes = nvVentes

    def salaire(self, taux):
        salaire_fixe = self.indSal * self.valSal
        salaire_interessement = taux * self.ventes
        return f"Salaire du matricule N°{self.matricule}: {salaire_fixe + salaire_interessement}$"


class Entreprise:
    valSal = 100

    def __init__(self):
        self.personnel = []

    def ajouter_personnel(self, pers):
        self.personnel.append(pers)

    def salaire_total(self, taux=0):
        total = 0
        for i in self.personnel:
            if isinstance(i, Commercial):
                total += (i.indSal * i.valSal) + (taux * i.ventes)
            else:
                total += (i.indSal * i.valSal)
        return f"Salaire total = {total}$"


employe1 = Employe("Alice", 101, 5)
employe2 = Employe("Bob", 102, 4)
employe3 = Employe("Charlie", 103, 3)

responsable1 = Responsable("Jean", 99, 7)
responsable2 = Responsable("Joe", 98, 8)

commercial = Commercial("David", 100, 6, 100)

responsable1.ajouter_inf(employe1)
responsable1.ajouter_inf(employe2)
responsable2.ajouter_inf(employe3)

entreprise = Entreprise()

entreprise.ajouter_personnel(commercial)
entreprise.ajouter_personnel(responsable1)
entreprise.ajouter_personnel(employe1)
entreprise.ajouter_personnel(employe2)
entreprise.ajouter_personnel(employe3)
print(entreprise.salaire_total(2.5))
