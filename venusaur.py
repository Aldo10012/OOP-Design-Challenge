from pokemon import Pokemon
from moves import Move

class Venusaur(Pokemon):
    def __init__(self, name, types):
        super().__init__(name, types)
        self.weakness = "fire"
        self.advantage = "water"

    def stengths_and_weaknesses(self):
        print(f"{self._name} is strong against {self.advantage} and weak against {self.weakness}")

    def fight(self, enemy):
        opponent = enemy

        # ends in draw
        if len(self._moves) == 0 and len(opponent._moves) == 0:
            print("draw") 
            return "draw"

        # ends in you winning
        elif len(self._moves) > 0 and len(opponent._moves) == 0:
            print(f"{self._name} wins!")
            return f"{self._name} wins!"

        # ends in opponent winning
        elif len(self._moves) == 0 and len(opponent._moves) > 0:
            print(f"{opponent._name} wins!")
            return f"{opponent._name} wins!"

        # we have a fight!
        else:
            print(f"\n{self._name}: hp = {self._health}, df = {self._deffense}  \n{opponent._name}: hp = {opponent._health}, df = {self._deffense}\n")
            
            while self.is_alive() and opponent.is_alive():
                your_move = None
                enemy_move = None

                ########################
                #   SELECT YOUR MOVE   #
                ########################
                print("------------------------------------------------------------------")
                print(f"\nSelect move for {self._name} to use")    
                ask_for_move = f""

                i = 1
                for move in self._moves:
                    ask_for_move += f"  [{i}] {move.name} \n"
                    i += 1
                ask_for_move += f"Pick your move: "

                pick_move = input(ask_for_move)

                if pick_move == "1":
                    your_move = self._moves[0]
                elif pick_move == "2":
                    your_move = self._moves[1]
                elif pick_move == "3":
                    your_move = self._moves[2]
                elif pick_move == "4":
                    your_move = self._moves[3]
                

                ############################
                #   SELECT OPPONENT MOVE   #
                ############################
                print(f"\nSelect move for {opponent._name} to use")    

                ask_for_enemy_move = f""
                i = 1
                for move in opponent._moves:
                    ask_for_enemy_move += f"  [{i}] {move.name} \n"
                    i += 1
                ask_for_enemy_move += f"Pick your move: "

                pick_enemy_move = input(ask_for_enemy_move)  

                if pick_enemy_move == "1":
                    enemy_move = opponent._moves[0]
                elif pick_enemy_move == "2":
                    enemy_move = opponent._moves[1]
                elif pick_enemy_move == "3":
                    enemy_move = opponent._moves[2]
                elif pick_enemy_move == "4":
                    enemy_move = opponent._moves[3]
                

                print(f"\n{self._name} selected {your_move.name} [type: {your_move.type} power: {your_move.power}]")
                print(f"{opponent._name} selected {enemy_move.name} [type: {enemy_move.type} power: {enemy_move.power}]")

                ################################
                #   POKEMON ATTACK EACHOTHER   #
                ################################

                # reduce deffence if weak to attack
                if self.weakness == enemy_move.type:
                    self._deffense /= 2
                if opponent.weakness == your_move.type:
                    opponent._deffense /= 2
                
                

                self.take_damage( opponent.use( enemy_move ) )
                opponent.take_damage( self.use ( your_move ) ) 

                print(f"\n{self._name}: hp = {self._health}  \n{opponent._name}: hp = {opponent._health}")

                if self.is_alive() == True and opponent.is_alive() == False:
                    print(f"\n{self._name} wins!")
                    return f"{self._name} wins!"
                
                if self.is_alive() == False and opponent.is_alive() == True:
                    print(f"\n{opponent._name} wins!")
                    return f"{opponent._name} wins!"
                
                if self.is_alive() == False and opponent.is_alive() == False:
                    print(f"\nDouble KO")
                    return f"Double KO"




if __name__ == "__main__":

    # List of moves
    petal_dance = Move("petal dance", "grass", 120)
    vine_whip   = Move("vine whip", "grass", 45)
    razor_leaf    = Move ("razor leaf", "grass", 55)
    double_edge   = Move("double edge", "normal", 120)

    # creating pokemon
    venusaur = Venusaur("Venusaur", ["fire", "flying"])
    venusaur.setEVs(80, 80, 100)
    venusaur.addMove( vine_whip )
    venusaur.addMove( petal_dance )
    # venusaur.use( vine_whip )


    venusaur2 = Venusaur("grassPoke", ["fire", "flying"])
    venusaur2.setEVs(200,80,90)
    venusaur2.addMove( vine_whip )

    venusaur.fight(venusaur2)
