from pokemon import Pokemon
from moves import Move

class Blastoise(Pokemon):
    def __init__(self, name, types, weakness):
        super().__init__(name, types, weakness)
        self.advantage = "water"

    def stengths_and_weaknesses(self):
        print(f"{self._name} is strong against {self.advantage} and weak against {self.weakness}")

    
    def hobby(self):
        print(f"{self._name} likes to nap inside of his shell.")

if __name__ == "__main__":

    # List of moves
    flash_cannon = Move("flash cannon", "steel", 80)
    rapid_spin   = Move("rapid spin", "normal", 50)
    aqua_tail    = Move ("aqua tail", "water", 90)
    hydro_pump   = Move("hydro pump", "water", 110)

    # creating pokemon
    blastoise = Blastoise("Blastoise", "water", "grass")
    blastoise.setEVs(100,25,200)
    blastoise.addMove( flash_cannon )
    blastoise.addMove( hydro_pump )

    shell_shucker = Blastoise("Shell Shucker", "water", "grass")
    shell_shucker.setEVs(100,25,200)
    shell_shucker.addMove( flash_cannon )
    shell_shucker.addMove( hydro_pump )
    shell_shucker.addMove( aqua_tail )
    # print(charizard.moves)

    blastoise.fight(shell_shucker)