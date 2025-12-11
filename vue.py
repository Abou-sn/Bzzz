import tkiteasy as tke
from constantes import NCASES
L,H = 1024,800
g = tke.ouvrirFenetre(L,H)

for x in range (0,L,L//NCASES):
    for y in range(0,H,H//NCASES) :
        g.dessinerLigne(x,y,x,H,'white')
        g.dessinerLigne(x,y,L,y,'white')

g.attendreTouche()
g.fermerFenetre()