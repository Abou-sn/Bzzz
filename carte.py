import constantes as cst
from random import randint
from libGrille import ouvrirFenetreGrille


g = ouvrirFenetreGrille(cst.TAILLE_CARTE,cst.NCASES,cst.NCASES)

def colorier_carte() :
    # On colorie les ruches
    for x in range(4):
        for y in range (4) :
            g.changerCarre(x,y,'blue')
            g.changerCarre(cst.NCASES-1-x,y,'green')
            g.changerCarre(x,cst.NCASES-1-y,'red')
            g.changerCarre(cst.NCASES-1-x,cst.NCASES-1-y,'pink')

    # On colorie la zone hors des ruches
    for x in range (16):
        for y in range(16):
            if g.getCouleur(x,y) not in ['blue','green','red','pink'] :
                g.changerCarre(x,y,'LawnGreen')
colorier_carte()

def placer_fleur(x,y):
    if g.getCouleur(x,y) not in ['blue','green','red','pink'] :
        for i in range (16):
            for j in range(16) :
                g.changerCarre(x,y,'white')
                g.changerCarre(cst.NCASES-1-x,y,'white')
                g.changerCarre(x,cst.NCASES-1-y,'white')
                g.changerCarre(cst.NCASES-1-x,cst.NCASES-1-y,'white')
for i in range (4) :
    placer_fleur(randint(0,16),randint(0,16))

g.attendreTouche()
g.fermerFenetre()

