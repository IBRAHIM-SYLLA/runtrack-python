import pygame
import sys
from Grille import Grille

class Jeu:
    def __init__(self) -> None:
        # La taille de la fenetre
        self.ecran = pygame.display.set_mode((600,600))
        # Le titre du jeu
        pygame.display.set_caption('Tic Tac Toe')
        # Variable jeu en cours
        self.jeu_encours = True
        # instance de la grille
        self.grille = Grille(self.ecran)
        # fixer les variables 'X' et '0'
        self.player_X = 'X'
        self.player_O = 'O'

        # on fix le compteur
        self.compteur = 0

    def fonction_principale(self):
        while self.jeu_encours:
            # On gère les events
            # boucle for avec la méthode qui va nous perlettre de recevoir les event et de les gérer
            for event in pygame.event.get():
                # si on veut quitté le jeu
                if event.type == pygame.QUIT:
                    sys.exit()

                # l'event qui correspond au clique droit. l'index [0] correspond au clic droit dans la liste des bouton de la souris
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    # obtenir la position de la souris
                    position = pygame.mouse.get_pos()
                    # l'opérateur // signifie division entière. Grace a ça chaque case aura sont propre "index"
                    position_x, position_y = position[0] // 200, position[1] // 200
                    print(position_x, position_y)
                    # condition si le compteur et pair ou impair
                    if self.compteur %2 == 0:
                        # fixé les valeurs
                        self.grille.fixer_la_valeur(position_x, position_y, self.player_X)
                    else:
                        self.grille.fixer_la_valeur(position_x, position_y, self.player_O)
                    self.compteur += 1
                    # print la grille
                    self.grille.print_grille()

            # on attribue une couleur a l'écran
            self.ecran.fill((255,211,155))
            # on affiche la grille
            self.grille.afficher()
            # on met a jour l'ecran
            pygame.display.flip()