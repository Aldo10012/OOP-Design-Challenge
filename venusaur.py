from pokemon import Pokemon
from moves import Move

class Venusaur(Pokemon):
    def __init__(self, name, types, weakness):
        super().__init__(name, types, weakness)
        self.advantage = "water"

    def stengths_and_weaknesses(self):
        print(f"{self._name} is strong against {self.advantage} and weak against {self.weakness}")

    def hobby(self):
        print(f"{self._name} likes to grow trees.")


if __name__ == "__main__":

    # List of moves
    petal_dance = Move("petal dance", "grass", 120)
    vine_whip   = Move("vine whip", "grass", 45)
    razor_leaf    = Move ("razor leaf", "grass", 55)
    double_edge   = Move("double edge", "normal", 120)

    # creating pokemon
    venusaur = Venusaur("Venusaur", "grass", "fire")
    venusaur.setEVs(80, 80, 100)
    venusaur.addMove( vine_whip )
    venusaur.addMove( petal_dance )
    # venusaur.use( vine_whip )


    venusaur2 = Venusaur("grassPoke", "grass", "fire")
    venusaur2.setEVs(200,80,90)
    venusaur2.addMove( vine_whip )

    venusaur.hobby()
    venusaur.fight(venusaur2)
