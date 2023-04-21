from Livre import Livre
from Auteur import Auteur
from Bibliotheque import Bibliotheque
from Client import Client

livres = [
    Livre("20,000 lieues sous les mers", Auteur("Vernes", "Jules")),
    Livre("1984", Auteur("Orwell", "Georges")),
    Livre("Le Petit Prince", Auteur("de St-Exupery", "Antoine"))
]

c = Client("Sylla", "Ibra", {})
b = Bibliotheque("La Biblio", {
    livres[0]: 9,
    livres[1]: 4,
    livres[2]: 11
})

# Catalogue avant la location
for l in b.catalogue:
    print(l)
print("\n")

# Le client loue le livre "1984"
b.louer(c, "1984")

# Catalogue après la location
for l in b.catalogue:
    print(l)

# Collection du client
print('\nCollection du client \n')
c.inventaire()
print('\n')

# Le client rend ses livres
b.rendreLivres(c)

# Collection du client après le retour des livres
c.inventaire()

# Collection du catalogue après le retour des livres
for l in b.catalogue:
    print(l)