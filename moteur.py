import constantes as cst
from classes import Ruche, Fleurs, Ouvriere, Bourdon, Eclaireuse
from random import randint
import tkiteasy as tke
from typing import Any

class Jeu:
    def __init__(self):
        #Création de la grille vide
        # On précise que c'est une liste de listes contenant "N'importe quoi" (Any)
        self.grille: list[list[Any]] = [[None for y in range(cst.NCASES)] for x in range(cst.NCASES)]
        self.fenetre = tke.ouvrirFenetre(cst.TAILLE_FENETRE, cst.TAILLE_FENETRE) #Créer la fenêtre
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
    def run(self):
        touche = self.fenetre.attendreTouche()
        while touche != 'Escape':
            touche = self.fenetre.attendreTouche()
        self.fenetre.fermerFenetre()
    def afficher(self):
        #Colorier le fond
        self.fenetre.dessinerRectangle(0,0,cst.TAILLE_FENETRE,cst.TAILLE_FENETRE,'lightblue')
        # Dessiner la grille
        for x in range(0,cst.TAILLE_FENETRE,cst.TAILLE_CASES):
            for y in range(0,cst.TAILLE_FENETRE,cst.TAILLE_CASES):
                self.fenetre.dessinerLigne(x,0,x,cst.TAILLE_FENETRE,'blue')
                self.fenetre.dessinerLigne(0,y,cst.TAILLE_FENETRE,y,'blue')
        # Dessiner les ruches
        for x in range (0,cst.TAILLE_CASES*4,cst.TAILLE_CASES):
            for y in range (0,cst.TAILLE_CASES*4,cst.TAILLE_CASES):
                self.fenetre.dessinerRectangle(x,y,cst.TAILLE_CASES,cst.TAILLE_CASES,'brown') #Ruche Joueur 1
                self.fenetre.dessinerRectangle(cst.TAILLE_FENETRE - cst.TAILLE_CASES - x, y,cst.TAILLE_CASES, cst.TAILLE_CASES, 'red') #Ruche Joueur 2
                self.fenetre.dessinerRectangle(cst.TAILLE_FENETRE - cst.TAILLE_CASES - x, cst.TAILLE_FENETRE - cst.TAILLE_CASES - y, cst.TAILLE_CASES, cst.TAILLE_CASES, 'green') #Ruche Joueur 3
                self.fenetre.dessinerRectangle(x,cst.TAILLE_FENETRE - cst.TAILLE_CASES - y, cst.TAILLE_CASES, cst.TAILLE_CASES, 'yellow') #Ruche Joueur 4
        # Dessiner les fleurs
        for fleur in self.fleurs:
            self.fenetre.dessinerRectangle(fleur.x * cst.TAILLE_CASES, fleur.y * cst.TAILLE_CASES, cst.TAILLE_CASES, cst.TAILLE_CASES, 'pink')
            


partie = Jeu()
partie.afficher()
partie.run()
