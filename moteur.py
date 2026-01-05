import constantes as cst
from classes import Ruche, Fleurs, Ouvriere, Bourdon, Eclaireuse
from random import randint
from typing import Any

class Jeu:
    def __init__(self):
        #Création de la grille vide
        # On précise que c'est une liste de listes contenant "N'importe quoi" (Any)
        self.grille: list[list[Any]] = [[None for y in range(cst.NCASES)] for x in range(cst.NCASES)]
        self.placer_ruches()
        
        #listes des objets
        self.ruches = []
        self.fleurs = []
        self.abeilles = []

    def placer_ruches(self):
        # Ruche Joueur 1 (Haut-Gauche)
        r1 = Ruche(0, 0, 1)
        self.ruches.append(r1)
        self.grille[0][0] = r1  # On la place sur la grille

        # Ruche Joueur 2 (Haut-Droite)
        r2 = Ruche(cst.NCASES - 1, 0, 2)
        self.ruches.append(r2)
        self.grille[cst.NCASES - 1][0] = r2

        # Ruche Joueur 3 (Bas-Droite)
        r3 = Ruche(cst.NCASES - 1, cst.NCASES - 1, 3)
        self.ruches.append(r3)
        self.grille[cst.NCASES - 1][cst.NCASES - 1] = r3

        # Ruche Joueur 4 (Bas-Gauche)
        r4 = Ruche(0, cst.NCASES - 1, 4)
        self.ruches.append(r4)
        self.grille[0][cst.NCASES - 1] = r4

partie = Jeu()
print(partie.grille)
partie.placer_ruches()
print(partie.grille)
