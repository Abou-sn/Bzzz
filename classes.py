import constantes as cst
from random import randint
class Abeilles :
    def __init__ (self,joueur : int ,x :int, y :int) -> None :
        self.joueur = joueur
        self.qte_points = 0
        self.x = x
        self.y = y
        self.etat = 'OK'
        self.directions_possibles = [(0, -1),(0, 1), (-1, 0), (1, 0)] #Les 4 directions possibles pour une ouvrière et un bourdon

    def peut_aller_vers(self, cible_x: int, cible_y: int) -> bool:
        """Vérifie si l'abeille peut aller vers la case (x,y). Renvoie True si c'est possible."""
        #On calcule le vecteur de déplacement
        dx = cible_x - self.x
        dy = cible_y - self.y
        
        if (dx, dy) in self.directions_possibles:
            return True
        return False
    

    def deplacer_vers_case(self, cible_x: int, cible_y: int) -> bool:
        """Tente de déplacer l'abeille vers la case (x,y). Renvoie True si réussi."""
        if self.peut_aller_vers(cible_x, cible_y): #Renvoi True
            #On effectue le déplacement
            self.x = cible_x
            self.y = cible_y
            return True
        return False

class Ouvriere (Abeilles) :
    def __init__(self, joueur : int, x : int, y : int) -> None:
        super().__init__(joueur, x, y)
        self.force = 1
        self.qte_nectar_max = 12
        self.image = 'sprites/ouvriere.png'
    
    def __repr__(self) -> str:
        return f"O{self.joueur}"
    
class Bourdon (Abeilles) :
    def __init__(self, joueur : int, x : int, y : int) -> None:
        super().__init__(joueur, x, y)
        self.force = 5
        self.qte_nectar_max = 1
        self.image = 'sprites/bourdon.png'

    def __repr__(self) -> str:
        return f"B{self.joueur}"

class Eclaireuse (Abeilles) :
    def __init__(self, joueur : int, x : int, y : int) -> None:
        super().__init__(joueur, x, y)
        self.force = 1
        self.qte_nectar_max = 3
        self.directions_possibles = [(0, -1),(0, 1), (-1, 0), (1, 0)
                                     ,(-1, -1), (-1, 1), (1, -1), (1, 1)] #Les 8 directions possibles pour une éclaireuse
        self.image = 'sprites/eclaireuse.png'
    def __repr__(self) -> str:
        return f"E{self.joueur}"

class Fleurs :
    def __init__(self, x : int, y : int) -> None :
        self.x = x
        self.y = y
        self.qte_nectar = randint(1,cst.MAX_NECTAR)
    def __repr__(self) -> str:
        return "F"

class Ruche :
    def __init__(self, x : int , y : int , joueur : int) -> None:
        self.x = x
        self.y = y
        self.joueur = joueur
        self.stock_nectar = cst.NECTAR_INITIAL
    def __repr__(self) -> str:
        return f"R({self.joueur})"