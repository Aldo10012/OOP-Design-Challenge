from pokemon import Pokemon
from moves import Move

class Blastoise(Pokemon):
    def __init__(self, name, types):
        super().__init__(name, types)
        self.weakness = "grass"
        self.advantage = "fire"

    def stengths_and_weaknesses(self):
        print(f"{self._name} is strong against {self.advantage} and weak against {self.weakness}")

if __name__ == "__main__":

    # List of moves
    flash_cannon = Move("flash cannon", "steel", 80)
    rapid_spin   = Move("rapid spin", "normal", 50)
    aqua_tail    = Move ("aqua tail", "water", 90)
    hydro_pump   = Move("hydro pump", "water", 110)

    # creating pokemon
    blastoise = Blastoise("Blastoise", ["fire", "flying"])
    blastoise.addMove( flash_cannon )
    blastoise.addMove( hydro_pump )
    blastoise.use( hydro_pump )


    # print(charizard.moves)