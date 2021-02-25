from pokemon import Pokemon
from moves import Move

class Charizard(Pokemon):
    def __init__(self, name, types):
        super().__init__(name, types)
        self.weakness = "water"
        self.advantage = "grass"

    def stengths_and_weaknesses(self):
        print(f"{self._name} is strong against {self.advantage} and weak against {self.weakness}")



if __name__ == "__main__":

    # List of moves
    flame_thrower = Move("flame thrower", "fire", 90)
    dragon_breath = Move("dragon breath", "dragon", 60)
    ember         = Move ("ember", "fire", 40)
    fire_spin     = Move("fire spin", "fire", 35)

    # creating pokemon
    charizard = Charizard("Charizard", ["fire", "flying"])
    charizard.addMove( flame_thrower )
    charizard.addMove( ember )
    charizard.use( fire_spin )


    # print(charizard.moves)