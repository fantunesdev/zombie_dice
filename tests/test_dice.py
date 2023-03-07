from colorama import Back, Fore, Style

from zombie_dice.entities.dice import Dice


def test_when_dice_constructor_recieves_green_must_return_verde():
    new_dice = Dice('green')
    assert 'VERDE' in str(new_dice)


def test_when_dice_contructor_recieves_green_must_return_a_green_faces_list():
    new_dice = Dice('green')
    assert new_dice.faces == ['CÉREBRO', 'PEGADA', 'CÉREBRO', 'ESPINGARDA', 'PEGADA', 'CÉREBRO']


def test_when_dice_constructor_recieves_yellow_must_return_amarelo():
    new_dice = Dice('yellow')
    assert 'AMARELO' in str(new_dice)


def test_when_dice_contructor_recieves_yellow_must_return_a_yellow_faces_list():
    new_dice = Dice('yellow')
    assert new_dice.faces == ['ESPINGARDA', 'PEGADA', 'CÉREBRO', 'ESPINGARDA', 'PEGADA', 'CÉREBRO']


def test_when_dice_constructor_recieves_red_must_return_vermelho():
    new_dice = Dice('red')
    assert 'VERMELHO' in str(new_dice)


def test_when_dice_contructor_recieves_red_must_return_a_red_faces_list():
    new_dice = Dice('red')
    assert new_dice.faces == ['ESPINGARDA', 'PEGADA', 'ESPINGARDA', 'CÉREBRO', 'PEGADA', 'ESPINGARDA']


def test_when_play_dice_must_return_one_valid_face():
    new_dice = Dice('green')
    assert 'ESPINGARDA' or 'PEGADA' or 'CÉREBRO' in str(new_dice.play()) and str


def test_when_play_dice_must_return_a_string():
    new_dice = Dice('green')
    assert isinstance(new_dice.play(), str)


def test_when_play_dice_the_strign_len_is_not_bigger_than_30():
    new_dice = Dice('red')
    assert len(new_dice.play()) <= 30
