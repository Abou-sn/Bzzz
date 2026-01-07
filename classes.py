import constantes as cst
from random import randint
class Abeilles :
    def __init__ (self,joueur : int ,x :int, y :int) -> None :
        self.joueur = joueur
        self.qte_points = 0
        self.x = x
        self.y = y
        self.etat = 'OK'
    def deplacer (self, direction : str) -> None :
        dx, dy = cst.TOUCHES_DIR[direction]
        if 0<= self.x +dx < cst.NCASES :
            self.x += dx
        if 0<= self.y +dy < cst.NCASES :
            self.y += dy
class Ouvriere (Abeilles) :
    def __init__(self, joueur : int, x : int, y : int) -> None:
        super().__init__(joueur, x, y)
        self.force = 1
        self.qte_nectar_max = 12
    
    def __repr__(self) -> str:
        return f"O{self.joueur}"
class Bourdon (Abeilles) :
    def __init__(self, joueur : int, x : int, y : int) -> None:
        super().__init__(joueur, x, y)
        self.force = 5
        self.qte_nectar_max = 1

    def __repr__(self) -> str:
        return f"B{self.joueur}"

class Eclaireuse (Abeilles) :
    def __init__(self, joueur : int, x : int, y : int) -> None:
        super().__init__(joueur, x, y)
        self.force = 1
        self.qte_nectar_max = 3
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