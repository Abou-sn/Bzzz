import tkiteasy as tke
import constantes as cst

g = tke.ouvrirFenetre(cst.L,cst.H)
#On dessine les lignes
for x in range(0,cst.L,cst.L_CASES) :
    for y in range (0,cst.H,cst.H_CASES) :
        g.dessinerLigne(0,y,cst.L,y,'red')
        g.dessinerLigne(x,0,x,cst.H,'red')
#On colorie les cases
for x in range(0,cst.L_CASES*4 ,cst.L_CASES) :
    for y in range (0, cst.H_CASES*4, cst.H_CASES):
        g.dessinerRectangle(x, y, cst.L_CASES, cst.H_CASES, 'green')
 
        g.dessinerRectangle(cst.L-x-cst.L_CASES, y, cst.L_CASES, cst.H_CASES, 'yellow')

        g.dessinerRectangle(x, cst.H-y-cst.H_CASES, cst.L_CASES, cst.H_CASES, 'red')

        g.dessinerRectangle(cst.L-x-cst.L_CASES, cst.H-y-cst.H_CASES, cst.L_CASES, cst.H_CASES,'blue')
        

g.attendreClic()
g.fermerFenetre()