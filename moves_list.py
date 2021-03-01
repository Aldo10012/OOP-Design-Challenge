from enum import Enum
from moves import Move

class Moves_list(Enum):

    ########################
    #   Grass TYPE MOVES   #
    ########################
    petal_dance   = Move("petal dance", "grass", 120)
    vine_whip     = Move("vine whip", "grass", 45)
    razor_leaf    = Move ("razor leaf", "grass", 55)
    # double_edge   = Move("double edge", "normal", 120)


if __name__ == "__main__":
    print(Moves_list)
    print(Moves_list.vine_whip)
    print(Moves_list.vine_whip.name)
    print(Moves_list.vine_whip.value)