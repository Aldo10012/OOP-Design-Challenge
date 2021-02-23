class Pokemon():
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.moves = list()
        self.attack = 0
        self.deffense = 0
        self.health = 0

    def setATK(self):
        pass

    def setDEF(self):
        pass

    def setHP(self):
        pass
    
    def setMoves(self):
        pass
        



if __name__ == "__main__":
    charizard = Pokemon("Charizard", ["fire", "flying"])

    print(charizard.name)
    print(charizard.types)
    print(charizard.moves)
    print(charizard.attack)
    print(charizard.deffense)
    print(charizard.health)