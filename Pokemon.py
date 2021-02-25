from abc import ABC, abstractclassmethod
from moves import Move


class Pokemon(ABC):
    # @abstractclassmethod
    # def setEVs(self): pass

    # @abstractclassmethod
    # def addMove(self): pass

    # @abstractclassmethod
    # def use(self): pass

    def __init__(self, name, types):
        # attributes are protected
        self._name = name
        self._types = types
        self._moves = list()
        self._attack = 0
        self._deffense = 0
        self._health = 0

    def setEVs(self, attack, deffense, health):
        self._attack = attack
        self._deffense = deffense
        self._health = health

    def addMove(self, move):
        if len(self._moves) > 4:
            print("sorry, no more moves")
        else:    
           self._moves.append(move)
        
    def use(self, move): 
        if move in self._moves:
            print(f"{self._name} just use {move.name}, and it did {move.power} damage")
            return move.power
        else:
            print(f"{self._name} doesn't have that move. sorry")    

    def take_damage(self, damage):
        damage_taken = damage - self._deffense
        if damage_taken > 0:
            self._health -= damage_taken


if __name__ == "__main__":
    # List of moves
    petal_dance = Move("petal dance", "grass", 120)
    vine_whip   = Move("vine whip", "grass", 45)
    razor_leaf    = Move ("razor leaf", "grass", 55)
    double_edge   = Move("double edge", "normal", 120)

    # creating pokemon
    venusaur = Pokemon("Venusaur", ["fire", "flying"])
    venusaur.addMove( vine_whip )
    venusaur.addMove( petal_dance )
    venusaur.use( double_edge )