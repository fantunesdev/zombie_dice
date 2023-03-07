import random

from colorama import Back, Fore, Style


class Dice:
    def __init__(self, color: str):
        self.__color = color

    def __repr__(self):
        if self.__color == 'green':
            return f'{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} VERDE {Style.RESET_ALL}'
        elif self.__color == 'yellow':
            return f'{Back.YELLOW}{Fore.BLACK}{Style.BRIGHT} AMARELO {Style.RESET_ALL}'
        elif self.__color == 'red':
            return f'{Back.RED}{Fore.BLACK}{Style.BRIGHT} VERMELHO {Style.RESET_ALL}'
        else:
            raise ValueError

    @property
    def faces(self):
        if self.__color == 'green':
            return ['CÉREBRO', 'PEGADA', 'CÉREBRO', 'ESPINGARDA', 'PEGADA', 'CÉREBRO']
        elif self.__color == 'yellow':
            return ['ESPINGARDA', 'PEGADA', 'CÉREBRO', 'ESPINGARDA', 'PEGADA', 'CÉREBRO']
        elif self.__color == 'red':
            return ['ESPINGARDA', 'PEGADA', 'ESPINGARDA', 'CÉREBRO', 'PEGADA', 'ESPINGARDA']
        else:
            raise ValueError

    def play(self):
        if self.__color == 'green':
            color = Back.GREEN
        elif self.__color == 'yellow':
            color = Back.YELLOW
        elif self.__color == 'red':
            color = Back.RED
        else:
            raise ValueError

        return f'{color}{Fore.BLACK}{Style.BRIGHT} {random.choice(self.faces)} {Style.RESET_ALL}'
