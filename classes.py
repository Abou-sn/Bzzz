import constantes as cst
from random import randint
class Abeilles :
    def __init__ (self,x : int ,y :int) -> None :
        self.qte_points = 0
        self.x = x
        self.y = y
        self.etat = 'OK'

class Ouvriere (Abeilles) :
    def __init__(self, x : int, y : int) -> None:
        super().__init__(x, y)
        self.force = 1
        self.qte_nectar_max = 12
class Bourdon (Abeilles) :
    def __init__(self, x : int, y : int) -> None:
        super().__init__(x,y)
        self.force = 5
        self.qte_nectar_max = 1
class Eclaireuse (Abeilles) :
    def __init__(self, x : int, y : int) -> None:
        super().__init__(x,y)
        self.force = 1
        self.qte_nectar_max = 3

class Fleurs :
    def __init__(self, x : int, y : int) -> None :
        self.x = x
        self.y = y
        self.qte_nectar = randint(1,cst.MAX_NECTAR)

class Ruche :
    def __init__(self, x : int , y : int , player : int) -> None:
        self.x = x
        self.y = y
        self.player = player
        self.stock_nectar = cst.NECTAR_INITIAL
