class Abeilles :
    def __init__ (self,x,y,etat) :
        self.qte_points = 0
        self.x = x
        self.y = y
        self.etat = etat

class Ouvriere (Abeilles) :
    def __init__(self, x, y, etat, ):
        super().__init__(x, y, etat)
        self.force = 1
        self.qte_nectar_max = 12
class Bourdon (Abeilles) :
    def __init__(self, x, y, etat, ):
        super().__init__(x,y,etat)
        self.force = 5
        self.qte_nectar_max = 1
class Eclaireuse (Abeilles) :
    def __init__(self, x, y, etat):
        super().__init__(x,y,etat)
        self.force = 1
        self.qte_nectar_max = 3

e = Eclaireuse(5,5,"OK",qte)
print(e.qte_points)
e.qte_points +=2
print(e.qte_points)