import constantes as cst
from classes import Ruche, Fleurs, Ouvriere, Bourdon, Eclaireuse
from random import randint
from typing import Any

class Jeu:
    def __init__(self):
        #Création de la grille vide
        # On précise que c'est une liste de listes contenant "N'importe quoi" (Any)
        self.grille: list[list[Any]] = [[None for y in range(cst.NCASES)] for x in range(cst.NCASES)]
        
        #listes des objets
        self.ruches = []
        self.fleurs = []
        self.abeilles = []

        # Placer les ruches aux coins
        self.placer_ruches()
        self.placer_fleur()

        for _ in range(4):    
            self.creer_abeille("Ouvriere")

        self.creer_abeille("Bourdon")
        self.creer_abeille("Eclaireuse")

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

    def placer_fleur(self):
        cpt = 0
        while cpt < cst.NFLEURS:
            x = randint(0, cst.NCASES - 1)
            y = randint(0, cst.NCASES - 1)

            #Si la case est vide, donc pas de Ruche ou pas de fleur on place une fleur
            if self.grille[x][y] is None:
                fleur = Fleurs(x, y)
                self.fleurs.append(fleur)
                self.grille[x][y] = fleur
            cpt += 1
    def creer_abeille(self, type_abeille: str) -> None:
        for ruche in self.ruches:
            #On recupere les infos de la ruche du joueur
            x = ruche.x
            y = ruche.y
            joueur = ruche.joueur

            if type_abeille == "Ouvriere":
                abeille = Ouvriere(joueur, x, y)
            elif type_abeille == "Bourdon":
                abeille = Bourdon(joueur, x, y)
            elif type_abeille == "Eclaireuse":
                abeille = Eclaireuse(joueur, x, y)
            else:
                raise ValueError("Type d'abeille inconnu")
        
            self.abeilles.append(abeille)
            
partie = Jeu()
print(partie.grille)
print(f"Nombre total d'abeilles : {len(partie.abeilles)}")