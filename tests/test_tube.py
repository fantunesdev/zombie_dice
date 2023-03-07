from zombie_dice.entities.dice import Dice
from zombie_dice.entities.tube import Tube


def test_when_initialize_tube_has_13_dices():
    new_tube = Tube()
    assert len(new_tube.dices) == 13


def test_when_initialize_tube_dices_are_shuffled():
    new_tube = Tube()
    organized_dices = []
    for i in range(6):
        organized_dices.append(Dice('green'))
    for i in range(4):
        organized_dices.append(Dice('yellow'))
    for i in range(3):
        organized_dices.append(Dice('red'))

    assert organized_dices != new_tube.dices


def test_when_draw_dices_3_dices_are_gived():
    new_tube = Tube()
    assert len(new_tube.draw_dices()) == 3


def test_when_draw_dices_first_time_then_tube_has_10_dices():
    new_tube = Tube()
    new_tube.draw_dices()
    assert len(new_tube.dices) == 10


def test_when_draw_dices_second_time_then_tube_has_7_dices():
    new_tube = Tube()
    new_tube.draw_dices()
    new_tube.draw_dices()
    assert len(new_tube.dices) == 7


def test_when_draw_dices_third_time_then_tube_has_4_dices():
    new_tube = Tube()
    new_tube.draw_dices()
    new_tube.draw_dices()
    new_tube.draw_dices()
    assert len(new_tube.dices) == 4


def test_when_draw_dices_fourth_time_then_tube_has_1_dice():
    new_tube = Tube()
    new_tube.draw_dices()
    new_tube.draw_dices()
    new_tube.draw_dices()
    new_tube.draw_dices()
    assert len(new_tube.dices) == 1


def teste_when_draw_dices_fifth_time_then_tube_has_10_dices():
    new_tube = Tube()
    new_tube.draw_dices()
    new_tube.draw_dices()
    new_tube.draw_dices()
    new_tube.draw_dices()
    new_tube.draw_dices()
    assert len(new_tube.dices) == 10

