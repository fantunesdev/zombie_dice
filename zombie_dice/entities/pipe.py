import random

from zombie_dice.entities.dice import Dice


class Pipe:
    def __init__(self):
        self.dices = []
        self.__init_pipe()
        self.drawn = []

    def __init_pipe(self):
        self.dices = []
        for i in range(6):
            self.dices.append(Dice('green'))
        for i in range(4):
            self.dices.append(Dice('yellow'))
        for i in range(3):
            self.dices.append(Dice('red'))
        self.shake()

    def shake(self):
        random.shuffle(self.dices)

    def draw_dices(self):
        self.drawn = []
        while len(self.drawn) < 3:
            try:
                if len(self.dices) <= 1:
                    self.__init_pipe()
                drawn_index = random.randint(1, len(self.dices))
                self.drawn.append(self.dices[drawn_index])
                del(self.dices[drawn_index])
            except IndexError:
                continue
        return self.drawn
