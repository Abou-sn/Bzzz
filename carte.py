import constantes as cst
from random import randint
from libGrille import ouvrirFenetreGrille


g = ouvrirFenetreGrille(cst.TAILLE_CARTE,cst.NCASES,cst.NCASES)

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
# On place les fleurs, aleatoirement mais symétriquement

g.attendreClic()
g.fermerFenetre()

