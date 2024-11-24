import pytest
from player import Player, Bot
from main import Game

# (heap0, heap1), (heap, matches)
@pytest.mark.parametrize("heaps, valid_move", [
    ([1, 0], (0, 1)), # 1, 0 -> 0, 0 win
    ([0, 1], (1, 1)), # 0, 1 -> 0, 0 win
    ([2, 1], (0, 1)), # 2, 1 -> 1, 1
    ([1, 2], (1, 1)), # 1, 2 -> 1, 1
    ([10, 12], (1, 2)), # 10, 12 -> 2, 12
    ([1, 12], (1, 11)), # 1, 12 -> 1, 1
    ([2, 1], (0, 1)),
])
def test_bot(heaps, valid_move):
    heap1, heap2 = heaps
    game = Game(heap1, heap2)
    bot = Bot()
    bot_generated_move = bot.make_move(game.heaps[0], game.heaps[1])
    assert game.valid_move(*bot_generated_move)
    assert bot_generated_move == valid_move