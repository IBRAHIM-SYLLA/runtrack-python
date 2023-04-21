from Livre import Livre
from Auteur import Auteur
from Client import Client

class Bibliotheque:
    def __init__(self, nom: str, catalogue: dict[Livre, int]) -> None:
        self.nom = nom
        self.catalogue = catalogue

    def acheterLivre(self, auteur: Auteur, nom: str, qt: int):
        for livre in auteur.oeuvres:
            if livre.titre == nom:
                self.catalogue[livre] = qt

    def inventaire(self) -> dict[Livre, int]:
        print(self.catalogue)
        return self.catalogue

    def louer(self, client: Client, nom: str):
        for livre in self.catalogue:
            if livre.titre == nom and self.catalogue[livre] > 0:
                client.collection[livre] = 1
                self.catalogue[livre] -= 1

    def rendreLivres(self, client: Client):
        for livre in client.collection:
            if client.collection[livre] > 0:
                self.catalogue[livre] = client.collection[livre]
                client.collection[livre] = 0