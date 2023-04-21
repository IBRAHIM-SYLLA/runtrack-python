from Personne import Personne
from job01 import Livre
class Auteur(Personne):
    def __init__(self, nom, prenom, oeuvres: list[Livre] = []) -> None:
        super().__init__(nom, prenom)
        self.oeuvres = oeuvres

    def listerOeuvre(self):
        for o in self.oeuvres:
            print(o)

    def ecrireUnLivre(self, titre) -> Livre:
        nouveau_livre = Livre(titre, self)
        self.oeuvres.append(nouveau_livre)
        return nouveau_livre