from Personne import Personne
from Livre import Livre

class Client(Personne):
    def __init__(self, nom, prenom, collection: dict[Livre, int]):
        super().__init__(nom, prenom)
        self.collection = collection

    def inventaire(self):
        for l in self.collection:
            print(l)