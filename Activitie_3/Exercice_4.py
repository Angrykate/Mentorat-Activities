class Pokemon:
    def __init__(self, nom, hp, atk):
        self.__nom = nom
        self.__hp = hp
        self.__atk = atk

    def getNom(self):
        return self.__nom

    def getHp(self):
        return self.__hp

    def getAtk(self):
        return self.__atk

    def isDead(self):
        return self.__hp == 0

    def attaquer(self, p):
        p.__hp -= self.__atk
        if p.__hp < 0:
            p.__hp = 0

    def afficher(self):
        print(f"Nom: {self.__nom} , HP: {self.__hp} , ATK: {self.__atk}")


class PokemonFeu(Pokemon):
    def attaquer(self, p):
        facteur = 1
        if isinstance(p, PokemonPlante):
            facteur = 2
        elif isinstance(p, PokemonFeu) or isinstance(p, PokemonEau):
            facteur = 0.5
        p._Pokemon__hp -= facteur * self.getAtk()
        if p._Pokemon__hp < 0:
            p._Pokemon__hp = 0

    def getClass(self):
        return self.__class__

    def getName(self):
        return self.__class__.__name__

    def getSimpleName(self):
        return self.__class__.__name__


class PokemonEau(Pokemon):
    def attaquer(self, p):
        facteur = 1
        if isinstance(p, PokemonFeu):
            facteur = 2
        elif isinstance(p, PokemonPlante) or isinstance(p, PokemonEau):
            facteur = 0.5
        p._Pokemon__hp -= facteur * self.getAtk()
        if p._Pokemon__hp < 0:
            p._Pokemon__hp = 0

    def getClass(self):
        return self.__class__

    def getName(self):
        return self.__class__.__name__

    def getSimpleName(self):
        return self.__class__.__name__


class PokemonPlante(Pokemon):
    def attaquer(self, p):
        facteur = 1
        if isinstance(p, PokemonEau):
            facteur = 2
        elif isinstance(p, PokemonFeu) or isinstance(p, PokemonPlante):
            facteur = 0.5
        p._Pokemon__hp -= facteur * self.getAtk()
        if p._Pokemon__hp < 0:
            p._Pokemon__hp = 0

    def getClass(self):
        return self.__class__

    def getName(self):
        return self.__class__.__name__

    def getSimpleName(self):
        return self.__class__.__name__


def choisir_Pokemon():
    pokemons = [
        Pokemon("Leuphorie", 390, 70),
        Pokemon("Ronflex", 430, 60),
        PokemonPlante("Bulbizarre", 400, 55),
        PokemonPlante("Florizarre", 300, 70),
        PokemonFeu("Dracaufeu", 700, 120),
        PokemonFeu("Salamèche", 390, 80),
        PokemonEau("Carapuce", 440, 75),
        PokemonEau("Carabaffe", 450, 80)
    ]
    print("Choisissez votre Pokémon :")
    for i, pok in enumerate(pokemons):
        type_pok = "Normal"
        if isinstance(pok, PokemonFeu):
            type_pok = "Feu"
        elif isinstance(pok, PokemonEau):
            type_pok = "Eau"
        elif isinstance(pok, PokemonPlante):
            type_pok = "Plante"
        print(f"{i + 1}) {pok.getNom()} (Type: {type_pok})\n")

    choix = 0
    while choix not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        choix = input("Entrez le numéro de votre choix : ")
    return pokemons[int(choix) - 1]


def combat_pokemon(pokemon1, pokemon2):
    print("-" * 50)
    print(f"{pokemon1.getNom()} ({pokemon1.__class__.__name__}) VS {pokemon2.getNom()} ({pokemon2.__class__.__name__})\n")
    while not pokemon1.isDead() and not pokemon2.isDead():
        pokemon1.attaquer(pokemon2)
        print(f"{pokemon1.getNom()} attaque {pokemon2.getNom()}!")
        pokemon2.afficher()
        if pokemon2.isDead():
            print(f"{pokemon2.getNom()} est KO! {pokemon1.getNom()} gagne !")
            break

        pokemon2.attaquer(pokemon1)
        print(f"{pokemon2.getNom()} attaque {pokemon1.getNom()}!")
        pokemon1.afficher()
        if pokemon1.isDead():
            print(f"{pokemon1.getNom()} est KO! {pokemon2.getNom()} gagne !")
            break


# Programme principal
print("*** Bienvenue dans le combat Pokémon !***")
pokemon1 = choisir_Pokemon()
pokemon2 = choisir_Pokemon()
combat_pokemon(pokemon1, pokemon2)
