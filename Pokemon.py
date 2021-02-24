from abc import ABC, abstractclassmethod

class Pokemon(ABC):
    @abstractclassmethod
    def setEVs(self): pass

    @abstractclassmethod
    def addMove(self): pass
