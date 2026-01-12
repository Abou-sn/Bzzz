import constantes as cst
from classes import Ruche, Fleurs, Abeilles, Ouvriere, Bourdon, Eclaireuse
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

        self.compteur_tours = 0 # Compteur global de tours
        

        #listes des objets
        self.ruches = []
        self.fleurs = []
        self.abeilles = []

        # Placer les ruches aux coins
        self.placer_ruches()
        self.placer_fleur()

        # On calcule le nectar total présent sur le plateau au début
        self.nectar_total_initial = 0
        for fleur in self.fleurs:
            self.nectar_total_initial += fleur.qte_nectar

        


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

    def ponte(self, type_abeille: str) -> None:
        for ruche in self.ruches:
            #On recupere les infos de la ruche du joueur
            x = ruche.x
            y = ruche.y
            joueur = ruche.joueur

            if joueur == self.joueur_actuel and ruche.stock_nectar >= cst.COUT_PONTE and self.recuperer_abeille(x, y) is None:


                if type_abeille == "Ouvriere" or type_abeille == "o":
                    abeille = Ouvriere(joueur, x, y)
                elif type_abeille == "Bourdon" or type_abeille == "b":
                    abeille = Bourdon(joueur, x, y)
                elif type_abeille == "Eclaireuse"  or type_abeille == "e":
                    abeille = Eclaireuse(joueur, x, y)
                else :
                    print("Type d'abeille inconnu.")
                    return  # Type d'abeille inconnu on 
                self.abeilles.append(abeille)
                ruche.stock_nectar -= cst.COUT_PONTE
            else:
                pass  # La ruche n'a pas assez de nectar ou ce n'est pas son tour

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

    def butiner(self, abeille, fleur : Fleurs) -> None:
        """Permet à une abeille de butiner une fleur."""
        recolte = 0
        nectar_disponible = fleur.qte_nectar # Nectar disponible dans la fleur
        capacite_restante = abeille.qte_nectar_max - abeille.qte_points # Capacité restante de l'abeille

        if nectar_disponible >= cst.MAX_NECTAR * 2 // 3: # Si la fleur a au moins des 2/3 de nectar
            recolte = 3
        elif nectar_disponible >= cst.MAX_NECTAR // 3 and nectar_disponible < cst.MAX_NECTAR * 2 // 3: # Si la fleur a au moins 1/3 de nectar
            recolte = 2
        else :
            recolte = 1

        if capacite_restante <= abeille.qte_nectar_max:  # Si l'abeille à encore de la place
        
            abeille.qte_points += min(recolte, capacite_restante) #Dans le cas ou la recolte est plus grande que la capacite restante
            fleur.qte_nectar -= recolte
    
    def phase_butinage(self,abeille) -> None:
            x = abeille.x
            y = abeille.y
            # Vérifier si l'abeille est sur une fleur
            if abeille.joueur == self.joueur_actuel:
                if isinstance(self.grille[x][y], Fleurs):
                    print("Butinage en cours...")
                    fleur = self.grille[x][y]
                    self.butiner(abeille, fleur)
    
    def deposer_nectar(self, abeille):
            """Vérifie si l'abeille est sur sa ruche et dépose le nectar si oui."""
            x, y = abeille.x, abeille.y
            contenu = self.grille[x][y]
            
            # Si la case contient une ruche et que c'est celle du joueur
            if isinstance(contenu, Ruche) and contenu.joueur == abeille.joueur:
                if abeille.qte_points > 0:
                    # Transfert du nectar
                    contenu.stock_nectar += abeille.qte_points
                    print(f"Dépot de {abeille.qte_points} nectar dans la ruche !")
                    
                    # On vide l'abeille
                    abeille.qte_points = 0

    def verifier_fin_jeu(self):
        """
        Vérifie les 3 conditions de fin du jeu.
        Retourne (True, id_gagnant) si le jeu est fini.
        Retourne (False, None) si le jeu continue.
        """
        
        # 1. VICTOIRE BLITZKRIEG (Plus de 50% du nectar total)
        majorite = self.nectar_total_initial / 2
        for ruche in self.ruches:
            if ruche.stock_nectar > majorite:
                return True, ruche.joueur

        # 2. TIME OUT (Trop de tours)
        if self.compteur_tours >= cst.TIME_OUT:
            return True, self.trouver_meneur()

        # 3. PÉNURIE (Plus de nectar sur fleurs ni abeilles)
        nectar_en_jeu = 0
        for fleur in self.fleurs:
            nectar_en_jeu += fleur.qte_nectar
        
        for abeille in self.abeilles:
            nectar_en_jeu += abeille.qte_points
            
        if nectar_en_jeu == 0:
            return True, self.trouver_meneur()

        # Si aucune condition n'est remplie, on continue
        return False, None

    def trouver_meneur(self):
        """Retourne l'ID du joueur avec le plus de nectar dans sa ruche."""
        meilleur_joueur = None
        max_nectar = -1
        
        # En cas d'égalité, cette logique prend le premier trouvé (peut être affiné)
        for ruche in self.ruches:
            if ruche.stock_nectar > max_nectar:
                max_nectar = ruche.stock_nectar
                meilleur_joueur = ruche.joueur
        
        return meilleur_joueur
    
    def run(self):
        # Boucle principale du jeu
        jeu_en_cours = True
        while jeu_en_cours:
            self.afficher()
            fin_du_tour = False
            abeille_selectionnee = None
            abeilles_ayant_bouge = [] # Liste pour mémoriser qui a bougé ce tour-ci

            print(f"Tour du Joueur {self.joueur_actuel}")

            #Mouvement + Ponte + Fin de tour
            while not fin_du_tour:
                cpt += 1
                #Gestion du Clavier (Ponte, Fin de tour, Quitter)
                touche = self.fenetre.recupererTouche()
                if touche == 'Escape':
                    self.fenetre.fermerFenetre()
                    return
                elif touche in ['o', 'b', 'e']:
                    self.ponte(touche)
                    self.afficher()
                elif touche == 's':
                        fin_du_tour = True
                        print("Fin du tour validée !")
                        self.joueur_actuel = (self.joueur_actuel % 4) + 1
                        self.compteur_tours += 1

                #Gestion de la Souris (Sélection, Mouvement, Validation)
                clic = self.fenetre.recupererClic() # Non bloquant 
                
                if clic:
                    gx = clic.x // cst.TAILLE_CASES
                    gy = clic.y // cst.TAILLE_CASES
                    
                    abeille_cliquee = self.recuperer_abeille(gx, gy)
                
                    # Clic sur une de nos abeilles qui n'a pas encore bougé
                    if abeille_cliquee is not None and abeille_cliquee.joueur == self.joueur_actuel:
                        if abeille_cliquee not in abeilles_ayant_bouge:
                            abeille_selectionnee = abeille_cliquee
                            abeilles_ayant_bouge.append(abeille_cliquee)
                        else:
                            print("Cette abeille a déjà bougé ce tour-ci.")
                            info = self.fenetre.afficherTexte("Cette abeille a déjà bougé ce tour-ci.", cst.TAILLE_CARTE //2, cst.TAILLE_CARTE //2, 'red', 30)
                             # Attendre 1 seconde pour que le joueur puisse lire le message

                    # Si une abeille est sélectionnée et qu'on clique ailleurs
                    elif abeille_selectionnee is not None:
                        # On vérifie si la case est valide et autorisée
                        if 0 <= gx < cst.NCASES and 0 <= gy < cst.NCASES and self.case_autorisee(abeille_selectionnee, gx, gy):
                            # Déplacement
                            abeille_selectionnee.deplacer_vers_case(gx, gy)
                            self.phase_butinage(abeille_selectionnee)
                            self.deposer_nectar(abeille_selectionnee)
                            abeille_selectionnee = None  # Désélectionner après le déplacement
                            self.afficher()

                            est_fini, gagnant = self.verifier_fin_jeu()
                            
                            if est_fini:
                                self.afficher_ecran_fin(gagnant)
                                return
             #Dans le cas ou Time out est atteint ou plus de nectar en jeu               
            est_fini, gagnant = self.verifier_fin_jeu()
            if est_fini:
                    self.afficher_ecran_fin(gagnant)
                    return

    
    def afficher_ecran_fin(self, gagnant):
        self.fenetre.dessinerRectangle(100, 100, cst.TAILLE_CARTE-200, 200, 'white')
        self.fenetre.afficherTexte(f"VICTOIRE JOUEUR {gagnant} !", cst.TAILLE_CARTE//2, cst.TAILLE_CARTE//2, 'red', 40)
        self.fenetre.attendreTouche()
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
            
            
            self.fenetre.afficherImage(x, y , ab.image)

        # --- ZONNE D'INFORMATIONS (BANDEAU DROIT) ---
        # 1. Fond de la bannière
        self.fenetre.dessinerRectangle(
            cst.TAILLE_CARTE, 0, 
            cst.TAILLE_BANNIERE, cst.TAILLE_CARTE, 
            'blueviolet'
        )

        # 2. Affichage du Tour courant
        # On décale un peu le texte par rapport au bord 
        x_info = cst.TAILLE_CARTE + cst.TAILLE_BANNIERE // 2 
        y_info = 50
        
        couleur_actuelle = cst.COULEURS_JOUEURS[self.joueur_actuel]
        
        self.fenetre.afficherTexte(
            f"TOUR DU JOUEUR {self.joueur_actuel}", 
            x_info, y_info, 
            couleur_actuelle,
            taille=15
        )

        # Affichage des stocks de nectar
        y_info += 50 # On descend pour la ligne suivante
        self.fenetre.afficherTexte("Stocks de Nectar :", x_info, y_info, 'black')
        
        y_info += 30 

        for ruche in self.ruches:
            couleur_ruche = cst.COULEURS_JOUEURS[ruche.joueur]
            texte = f"Joueur {ruche.joueur} : {ruche.stock_nectar} points de nectar"
            
            self.fenetre.afficherTexte(texte, x_info, y_info, couleur_ruche)
            y_info += 30 
        
        y_info += 100
        ligne_sep = "-" * 30 
        Commande = f"Pour pondre une abeille appuyez  \n O (Ouvrière) \n B (Bourdon) \n E (Eclaireuse) \n {ligne_sep} \n Pour finir le tour : S \n {ligne_sep} \n  Pour quitter : Échap"
        self.fenetre.afficherTexte(Commande, x_info, y_info, 'white',10)

        y_info += 400
        self.fenetre.afficherTexte("Butinez les fleurs pour \n récolter du nectar !", x_info, y_info, 'white',10)
        


partie = Jeu()
partie.afficher_terminal()
partie.run()
