
class Livre:
    def  __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)

    def __str__(self):
        return f"Titre du livre écrit par {self.auteur}"

mon_livre = Livre("quoicoulivre", "quoicouIbra")
mon_livre.print()