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
        # On doit placer NFLEURS part quart de la carte 
        while cpt < cst.NFLEURS:
            # NCASES // 2 donne la moitié de la grille
            x = randint(0, cst.NCASES // 2 - 1)
            y = randint(0, cst.NCASES // 2 - 1)

            sur_ruche= (x < cst.TAILLE_BASE) and (y < cst.TAILLE_BASE)

            # La case doit être vide (pas de Ruche, pas d'autre fleur)
            if self.grille[x][y] is None and not sur_ruche:
                # Calcul des coordonnées des 3 reflets
                x2 = cst.NCASES - 1 - x
                y2 = cst.NCASES - 1 - y
                
                f1 = Fleurs(x, y)
                nectar_commun = f1.qte_nectar # On sauvegarde son nectar
                
                # Création des reflets avec la meme qte nectar
                f2 = Fleurs(x2, y)
                f2.qte_nectar = nectar_commun
                
                f3 = Fleurs(x, y2)
                f3.qte_nectar = nectar_commun
                
                f4 = Fleurs(x2, y2)
                f4.qte_nectar = nectar_commun
                
                # Ajout dans la liste des fleurs
                self.fleurs.extend([f1, f2, f3, f4])
                
                # Placement sur la grille
                self.grille[x][y] = f1
                self.grille[x2][y] = f2
                self.grille[x][y2] = f3
                self.grille[x2][y2] = f4
                
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

        # Dans moteur.py, dans la classe Jeu
    def afficher_terminal(self):
        for y in range(cst.NCASES):
            ligne = ""
            for x in range(cst.NCASES):
                contenu = self.grille[x][y]
                if contenu == None:
                    ligne = ligne + "-   "  # Un point pour le vide
                else:
                    ligne = ligne + str(contenu) + " " # L'objet s'il y en a un
            print(ligne)

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
        marge = (cst.TAILLE_CASES) // 4
        for fleur in self.fleurs:
            self.fenetre.afficherImage(fleur.x * cst.TAILLE_CASES + marge, fleur.y * cst.TAILLE_CASES + marge,'sprites/fleur.png')
            


partie = Jeu()
partie.afficher()
partie.run()
partie.afficher_terminal()
