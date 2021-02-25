from pokemon import Pokemon
from moves import Move

class Venusaur(Pokemon):
    def __init__(self, name, types):
        super().__init__(name, types)
        self.weakness = "fire"
        self.advantage = "water"

    def stengths_and_weaknesses(self):
        print(f"{self._name} is strong against {self.advantage} and weak against {self.weakness}")



        
        



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
    venusaur.use( vine_whip )


    # print(charizard.moves)