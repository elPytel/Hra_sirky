import random

class Player:
    def __init__(self, name="Player"):
        self.name = name

    def make_move(self, heap1_amount, heap2_amount):
        heap = int(input("Enter heap number: "))-1
        matches = int(input("Enter matches number: "))
        return heap, matches

class Bot(Player):
    def __init__(self, name="Bot"):
        super().__init__(name)

    def move_heaps_are_not_equal(self, heap0_amount, heap1_amount):
        """
        If the heaps are not equal, we can guarantee a win by:
        - winning move: 0,X -> 0,0
        - make the heaps equal: X+n, X -> X, X
        """
        heap = 0 if heap0_amount > heap1_amount else 1
        amount = abs(heap0_amount - heap1_amount)
        return heap, amount

    def move_heaps_are_equal(self, heap0_amount, heap1_amount):
        """
        If both heaps are the same we cannot guarantee a win.
        - random move.
        """
        heap = random.choice([0, 1])
        amount = 1
        return heap, amount

    def make_move(self, heap0_amount, heap1_amount):
        """
        For two heaps of matches, there are two possibilities:
        - the amounts of matches is same
        - the amounts of matches is different
        """
        if heap0_amount == heap1_amount:
            heap, amount = self.move_heaps_are_equal(heap0_amount, heap1_amount)
        
        if heap0_amount != heap1_amount:
            heap, amount = self.move_heaps_are_not_equal(heap0_amount, heap1_amount)

        print(f"Bot takes {amount} from heap {heap+1}")
        return heap, amount
    


