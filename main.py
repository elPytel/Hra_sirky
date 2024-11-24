import random
from colors import *
from player import Player, Bot

ASCII_ART = """
         , - ~ ~ ~ - ,                     , - ~ ~ ~ - ,
     , '               ' ,             , '               ' ,
   ,                       ,         ,                       ,
  ,                         ,       ,                         ,
 ,                           ,     ,                           ,
 ,             X1            ,     ,             X2            ,
 ,                           ,     ,                           ,
  ,                         ,       ,                         ,
   ,                       ,         ,                       ,
     ,                  , '            ,                  , '    
       ' - , _ _ _ ,  '                  ' - , _ _ _ ,  '
"""

class Game:
    def __init__(self, first_heap_amount, second_heap_amount):
        self.heaps = [first_heap_amount, second_heap_amount]
        pass

    def valid_move(self, heap, matches):
        return heap in [0, 1] and 0 < matches <= self.heaps[heap]
    
    def print_state(self):
        print("First heap X1: ", Blue+str(self.heaps[0])+NC)
        print("Second heap X2: ", Blue+str(self.heaps[1])+NC)
    
    def print_welcome(self):
        print("Welcome to the game take or loose!")
        print("The game is simple. There are two heaps of matches.")
        print("Players take turns taking matches from the heaps.")
        print("On each turn, a player must take at least one match.")
        print("The player who takes the last match wins.")
        print("Let's start!")
        print("Two heaps of matches:")
        print(ASCII_ART)

    def __str__(self) -> str:
        return f"Game({self.heaps[0]}, {self.heaps[1]})"

    def game_over(self):
        return self.heaps[0] == 0 and self.heaps[1] == 0


PLAYER_FIRST = True
MATHES_MIN = 10
MATHES_MAX = 15

def generate_amount_of_matches():
    return random.randint(MATHES_MIN, MATHES_MAX)

if __name__ == "__main__":
    heap1 = generate_amount_of_matches()
    heap2 = generate_amount_of_matches()
    game = Game(heap1, heap2)
    game.print_welcome()

    human_player = Player()
    bot = Bot()

    if PLAYER_FIRST:
        players = [human_player, bot]
    else:
        players = [bot, human_player]
    
    while not game.game_over():
        print(Green+"New turn!"+NC)
        for player in players:
            game.print_state()
            heap, matches = player.make_move(game.heaps[0], game.heaps[1])
            while not game.valid_move(heap, matches):
                print("Invalid move. Try again.")
                heap, matches = player.make_move(game.heaps[0], game.heaps[1])
            game.heaps[heap] -= matches

            if game.game_over():
                print(player.name, "wins!")
                break
