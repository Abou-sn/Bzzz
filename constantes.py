NCASES = 16
NFLEURS = 4
TAILLE_BASE = 4
NECTAR_INITIAL = 10
MAX_NECTAR = 45
TIME_OUT = 300
COUT_PONTE = 5
TIME_KO = 5
L,H = 1024,800
L_CASES = L//NCASES
H_CASES = H//NCASES
TOUCHES_DIR = {
    'Up': (0, -1),          
    'Down': (0, 1),
    'Left': (-1, 0),
    'Right': (1, 0)
    }

print(TOUCHES_DIR['Down'][0])