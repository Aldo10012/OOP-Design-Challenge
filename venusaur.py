from pokemon import Pokemon
from moves import Move

class Venusaur(Pokemon):
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.moves = list()
        self.attack = 0
        self.deffense = 0
        self.health = 0
    
    def setEVs(self, attack, deffense, health):
        self.attack = attack
        self.deffense = deffense
        self.health = health

    def addMove(self, move):
        if len(self.moves) > 4:
            print("sorry, no more moves")
        else:    
           self.moves.append(move)
        
    def use(self, move): 
        if move in self.moves:
            print(f"{self.name} just use {move.name}, and it did {move.power} damage")
            return move.power
        else:
            print(f"{self.name} doesn't have that move. sorry")    




if __name__ == "__main__":

    # List of moves
    petal_dance = Move("petal dance", "grass", 120)
    vine_whip   = Move("vine whip", "grass", 45)
    razor_leaf    = Move ("razor leaf", "grass", 55)
    double_edge   = Move("double edge", "normal", 120)

    # creating pokemon
    venusaur = Venusaur("Venusaur", ["fire", "flying"])
    venusaur.addMove( vine_whip )
    venusaur.addMove( petal_dance )
    venusaur.use( double_edge )


    # print(charizard.moves)