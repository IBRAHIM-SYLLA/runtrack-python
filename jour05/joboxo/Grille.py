import pygame
import sys

class Grille:
    def __init__(self, ecran) -> None:
        self.ecran = ecran
        # variable qui contien les ligne
        self.ligne = [((200,0), (200,600)),
                ((400,0), (400,600)),
                ((0,200), (600,200)),
                ((0,400), (600,400)),]
        # initier la grille
        self.grille = [[None for x in range(0, 3)] for y in range(0, 3)]

    # affiche les ligne
    def afficher(self):
        for ligne in self.ligne:
            # on dessine les lignes
            pygame.draw.line(self.ecran, (0, 0, 0), ligne[0], ligne[1], 2)

    # on print la grille
    def print_grille(self):
        print(self.grille)

    # fixé les valeurs x et y
    def fixer_la_valeur(self, x, y, valeur):
        self.grille[y][x] = valeur