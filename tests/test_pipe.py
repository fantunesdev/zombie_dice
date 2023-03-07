from zombie_dice.entities.dice import Dice
from zombie_dice.entities.pipe import Pipe


def test_when_initialize_pipe_has_13_dices():
    new_pipe = Pipe()
    assert len(new_pipe.dices) == 13


def test_when_initialize_pipe_dices_are_shuffled():
    new_pipe = Pipe()
    organized_dices = []
    for i in range(6):
        organized_dices.append(Dice('green'))
    for i in range(4):
        organized_dices.append(Dice('yellow'))
    for i in range(3):
        organized_dices.append(Dice('red'))

    assert organized_dices != new_pipe.dices


def test_when_draw_dices_3_dices_are_gived():
    new_pipe = Pipe()
    assert len(new_pipe.draw_dices()) == 3


def test_when_draw_dices_first_time_then_pipe_has_10_dices():
    new_pipe = Pipe()
    new_pipe.draw_dices()
    assert len(new_pipe.dices) == 10


def test_when_draw_dices_second_time_then_pipe_has_7_dices():
    new_pipe = Pipe()
    new_pipe.draw_dices()
    new_pipe.draw_dices()
    assert len(new_pipe.dices) == 7


def test_when_draw_dices_third_time_then_pipe_has_4_dices():
    new_pipe = Pipe()
    new_pipe.draw_dices()
    new_pipe.draw_dices()
    new_pipe.draw_dices()
    assert len(new_pipe.dices) == 4


def test_when_draw_dices_fourth_time_then_pipe_has_1_dice():
    new_pipe = Pipe()
    new_pipe.draw_dices()
    new_pipe.draw_dices()
    new_pipe.draw_dices()
    new_pipe.draw_dices()
    assert len(new_pipe.dices) == 1


def teste_when_pipe_has_1_dice_or_less_all_dices_goes_back_to_pipe_and_before_dawn_pipe_has_10_dices():
    new_pipe = Pipe()
    new_pipe.draw_dices()
    new_pipe.draw_dices()
    new_pipe.draw_dices()
    new_pipe.draw_dices()
    new_pipe.draw_dices()
    assert len(new_pipe.dices) == 10

