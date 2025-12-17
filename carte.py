import constantes as cst
from random import randint
from libGrille import ouvrirFenetreGrille


g = ouvrirFenetreGrille(cst.TAILLE_CASES,cst.NCASES,cst.NCASES)

def creer_carte() : 
    # On colorie les ruches
    for x in range(cst.TAILLE_BASE):
        for y in range (cst.TAILLE_BASE) :
            g.changerCarre(x,y,'blue')
            g.changerCarre(cst.NCASES-1-x,y,'green')
            g.changerCarre(x,cst.NCASES-1-y,'red')
            g.changerCarre(cst.NCASES-1-x,cst.NCASES-1-y,'pink')
    # On colorie la zone hors des ruches
    for x in range (cst.NCASES):
        for y in range(cst.NCASES):
            if g.getCouleur(x,y) not in ['blue','green','red','pink'] :
                g.changerCarre(x,y,'LawnGreen')


                
creer_carte()               
g.attendreTouche()
g.afficherImage(cst.TAILLE_CASES,cst.TAILLE_CASES,'../sprites/fleur.png')
g.attendreTouche()
g.fermerFenetre()

