from pokemon import Pokemon
from moves import Move

class Blastoise(Pokemon):
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
    flash_cannon = Move("flash cannon", "Steel", 80)
    rapid_spin   = Move("rapid spin", "normal", 50)
    aqua_tail    = Move ("aqua tail", "water", 90)
    hydro_pump   = Move("hydro pump", "water", 110)

    # creating pokemon
    blastoise = Blastoise("Blastoise", ["fire", "flying"])
    blastoise.addMove( flash_cannon )
    blastoise.addMove( hydro_pump )
    blastoise.use( hydro_pump )


    # print(charizard.moves)