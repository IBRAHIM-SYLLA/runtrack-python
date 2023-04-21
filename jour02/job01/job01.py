
class Livre:
    def  __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)

mon_livre = Livre("quoicoulivre", "quoicouIbra")
mon_livre.print()