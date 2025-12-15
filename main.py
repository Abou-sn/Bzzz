import carte
import constantes as cst
from libGrille import ouvrirFenetreGrille

g = ouvrirFenetreGrille(cst.TAILLE_CARTE,cst.NCASES,cst.NCASES)
carte.colorier_carte()
carte.placer_fleur(4,4)