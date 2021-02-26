from pokemon import Pokemon
from moves import Move

class Charizard(Pokemon):
    def __init__(self, name, types, weakness):
        super().__init__(name, types, weakness)
        self.advantage = "water"

    def stengths_and_weaknesses(self):
        print(f"{self._name} is strong against {self.advantage} and weak against {self.weakness}")


    def hobby(self):
        print(f"{self._name} likes to fly high above the clouds.")

if __name__ == "__main__":

    # List of moves
    flame_thrower = Move("flame thrower", "fire", 90)
    dragon_breath = Move("dragon breath", "dragon", 60)
    ember         = Move ("ember", "fire", 40)
    fire_spin     = Move("fire spin", "fire", 35)

    # creating pokemon
    charizard = Charizard("Charizard", "fire", "water")
    charizard.setEVs(100,40,20)
    charizard.addMove( flame_thrower )
    charizard.addMove( ember )
    # charizard.use( fire_spin )

    lilChar = Charizard("lil Char", "fire", "water")
    lilChar.setEVs(100,50,180)
    lilChar.addMove( flame_thrower )
    lilChar.addMove( dragon_breath )
    lilChar.addMove( ember )

    charizard.fight( lilChar )
