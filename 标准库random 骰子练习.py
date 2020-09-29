import random


class Dice:
    def roll(self):
        numbers = (1, 2, 3, 4, 5, 6)
        x = random.choice(numbers)
        y = random.choice(numbers)
        #return f'({x}, {y})'
        return x, y  # return 返回一个元组


shaizi = Dice()
print(shaizi.roll())
