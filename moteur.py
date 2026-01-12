import constantes as cst
from classes import Ruche, Fleurs, Ouvriere, Bourdon, Eclaireuse
from random import randint
import tkiteasy as tke
from typing import Any

class Jeu:
    def __init__(self):
        #Création de la grille vide
        # On précise que c'est une liste de listes pouvant contenir "N'importe quoi" (Any)
        self.grille: list[list[Any]] = [[None for y in range(cst.NCASES)] for x in range(cst.NCASES)]
        self.fenetre = tke.ouvrirFenetre(cst.TAILLE_CARTE+ cst.TAILLE_BANNIERE, cst.TAILLE_CARTE ) #Créer la fenêtre
        #Pour les tours de jeu
        self.joueur_actuel = 1
        
        #listes des objets
        self.ruches = []
        self.fleurs = []
        self.abeilles = []

        # Placer les ruches aux coins
        self.placer_ruches()
        self.placer_fleur()

        self.creer_abeille("Eclaireuse")

    def placer_ruches(self):
        taille = cst.TAILLE_BASE # 4
        n = cst.NCASES
        # Ruche Joueur 1 (Haut-Gauche)
        r1 = Ruche(0, 0, 1)
        self.ruches.append(r1)
        for x in range(taille):
            for y in range(taille):
                self.grille[x][y] = r1  # On la place sur la grille


        # Ruche Joueur 2 (Haut-Droite)
        r2 = Ruche(cst.NCASES - 1, 0, 2)
        self.ruches.append(r2)
        for x in range(n - taille, n):
            for y in range(taille):
                self.grille[x][y] = r2

        # Ruche Joueur 3 (Bas-Droite)
        r3 = Ruche(cst.NCASES - 1, cst.NCASES - 1, 3)
        self.ruches.append(r3)
        for x in range(n - taille, n):
            for y in range(n - taille, n):
                self.grille[x][y] = r3
        # Ruche Joueur 4 (Bas-Gauche)
        r4 = Ruche(0, cst.NCASES - 1, 4)
        self.ruches.append(r4)
        for x in range(taille):
            for y in range(n - taille, n):
                self.grille[x][y] = r4

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

    def afficher_terminal(self):
        for y in range(cst.NCASES):
            ligne = ""
            for x in range(cst.NCASES):
                contenu = self.grille[x][y]
                if contenu == None:
                    ligne = ligne + ".   "  # Un point pour le vide
                else:
                    ligne = ligne + str(contenu) + " " # L'objet s'il y en a un
            print(ligne)

    def case_autorisee(self, abeille, x: int, y: int) -> bool:
        """Vérifie si la case (x,y) est bloquante ou non. Renvoie True si la case est autorisée."""
        contenu = self.grille[x][y]

        # Si c'est une ruche ennemie
        if isinstance(contenu, Ruche) and contenu.joueur != abeille.joueur:
            return False

        # Vérification des autres abeilles 
        for autre_abeille in self.abeilles:
            # On vérifie si quelqu'un est déjà à cette position (x, y)
            if autre_abeille.x == x and autre_abeille.y == y: # Si c'est l'abeille elle-même, on l'ignore (Cas ou on reclique sur sa propre la case)
                if autre_abeille is not abeille:
                    return False
        return True

    def recuperer_abeille(self, x, y):
        """Renvoie l'abeille située en (x,y), ou None s'il n'y en a pas."""
        for ab in self.abeilles:
            if ab.x == x and ab.y == y:
                return ab
        return None

        

    def run(self):
        self.afficher()
        abeille = None
        
        while True:
             # Attendre un clic de souris   
            clic = self.fenetre.attendreClic()
            
            #On convertit en coordonnees de la grille
            gx = clic.x // cst.TAILLE_CASES
            gy = clic.y // cst.TAILLE_CASES

            abeille_cliquee = self.recuperer_abeille(gx, gy)

            if abeille_cliquee is not None and abeille_cliquee.joueur == self.joueur_actuel:
                # C'est une abeille qui a été cliquée
                
                    abeille = abeille_cliquee
            
            
            else : # Ce n'est pas une abeille, on tente de déplacer l'abeille sélectionnée
                if abeille is not None:

                    if 0 <= gx < cst.NCASES and 0 <= gy < cst.NCASES and self.case_autorisee(abeille, gx, gy):
                        abeille.deplacer_vers_case(gx, gy)
                        self.afficher()
                        self.joueur_actuel = (self.joueur_actuel % 4) + 1  # Passer au joueur suivant
                        abeille = None  # Désélectionner l'abeille après le déplacement
            
            #Pour gerer la fermeture de la fenetre  
            fermer = self.fenetre.recupererTouche()
            if fermer == 'Escape':
                break
        
        self.fenetre.fermerFenetre()

    def afficher(self):
        #Colorier le fond
        self.fenetre.dessinerRectangle(0,0,cst.TAILLE_CARTE,cst.TAILLE_CARTE,'lightblue')
        # Dessiner la grille
        for x in range(0,cst.TAILLE_CARTE,cst.TAILLE_CASES):
            for y in range(0,cst.TAILLE_CARTE,cst.TAILLE_CASES):
                self.fenetre.dessinerLigne(x,0,x,cst.TAILLE_CARTE,'blue')
                self.fenetre.dessinerLigne(0,y,cst.TAILLE_CARTE,y,'blue')
        # Dessiner les ruches
        for x in range (0,cst.TAILLE_CASES*cst.TAILLE_BASE,cst.TAILLE_CASES):
            for y in range (0,cst.TAILLE_CASES*cst.TAILLE_BASE,cst.TAILLE_CASES):
                self.fenetre.dessinerRectangle(x,y,cst.TAILLE_CASES,cst.TAILLE_CASES,cst.COULEURS_JOUEURS[1]) #Ruche Joueur 1
                self.fenetre.dessinerRectangle(cst.TAILLE_CARTE - cst.TAILLE_CASES - x, y,cst.TAILLE_CASES, cst.TAILLE_CASES, cst.COULEURS_JOUEURS[2]) #Ruche Joueur 2
                self.fenetre.dessinerRectangle(cst.TAILLE_CARTE - cst.TAILLE_CASES - x, cst.TAILLE_CARTE - cst.TAILLE_CASES - y, cst.TAILLE_CASES, cst.TAILLE_CASES, cst.COULEURS_JOUEURS[3]) #Ruche Joueur 3
                self.fenetre.dessinerRectangle(x,cst.TAILLE_CARTE - cst.TAILLE_CASES - y, cst.TAILLE_CASES, cst.TAILLE_CASES, cst.COULEURS_JOUEURS[4]) #Ruche Joueur 4
        # Dessiner les fleurs
        marge = (cst.TAILLE_CASES) // 2-30 # Pour centrer l'image dans la case, la valeur 30 dépend de la taille de l'image qui est de 60x60
        for fleur in self.fleurs:
            self.fenetre.afficherImage(fleur.x * cst.TAILLE_CASES + marge, fleur.y * cst.TAILLE_CASES + marge,'sprites/fleur.png')
        
        for ab in self.abeilles:
            # Calcul de la position pixel
            x = ab.x * cst.TAILLE_CASES
            y = ab.y * cst.TAILLE_CASES
            
            
            # On dessine un carré centré, un peu plus petit que la case (marge de 10)
            marge = 10
            taille_abeille = cst.TAILLE_CASES - (marge * 2)
            
            self.fenetre.afficherImage(x, y , ab.image)


partie = Jeu()
partie.afficher_terminal()
partie.run()
 