from moves import Move

class Pokemon():
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
        self.moves.append(move)
        



if __name__ == "__main__":

    # List of moves
    flame_thrower = Move("flame thrower", "fire", 90)
    dragon_breath = Move("dragon breath", "fire", 60)
    ember         = Move ("ember", "fire", 40)
    fire_spin     = Move("fire spin", "fire", 35)

    charizard = Pokemon("Charizard", ["fire", "flying"])
    charizard.addMove( flame_thrower )
    charizard.addMove( dragon_breath )
    charizard.addMove( ember )
    charizard.addMove( fire_spin )


    print(charizard.moves)
    