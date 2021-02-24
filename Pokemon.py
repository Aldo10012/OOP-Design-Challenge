from abc import ABC, abstractclassmethod
from moves import Move


# class Pokemon():
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.moves = list()
#         self.attack = 0
#         self.deffense = 0
#         self.health = 0

#     def setEVs(self, attack, deffense, health):
#         self.attack = attack
#         self.deffense = deffense
#         self.health = health

    
#     def addMove(self, move):
#         if len(self.moves) > 4:
#             print("sorry, no more moves")
#         else:    
#            self.moves.append(move)
        
#     def use(self, move): 
#         if move in self.moves:
#             print(f"{self.name} just use {move.name}, and it did {move.power} damage")
#             return move.power
#         else:
#             print(f"{self.name} doesn't have that move. sorry")



class Pokemon(ABC):
    @abstractclassmethod
    def setEVs(self): pass

    @abstractclassmethod
    def addMove(self): pass



class Charizard(Pokemon):
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
    