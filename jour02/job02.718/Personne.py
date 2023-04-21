class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("nom: " + self.nom)
        print("prenom: " + self.prenom)

    def _get_nom_prenom(self):
        print('récupération du nom et du prénom')
        return self.nom + ' ' + self.prenom

    def _set_nom_prenom(self, v):
        print("Changement du nom et du prenom")
        self.nom = v
        self.prenom = v

    def __str__(self):
        return f"Titre du livre écrit par {self.nom} {self.prenom}"

    nom_prenom = property(_get_nom_prenom, _set_nom_prenom)

p = Personne("Sylla", "ibra")
p.nom = "Ib"
p.SePresenter()