import pygame
import json
from time import sleep


class Morse:
    def __init__(self):
        with open('./codes.json') as json_file:
            self.codes = json.load(json_file)
        pygame.mixer.init()
        self.code = ''
        self.text: str = ''

    def play(self):
        for c in self.code:
            if c == '.':
                pygame.mixer.music.load("./audio/dit.ogg")
                pygame.mixer.music.play(loops=0)
            elif c == '-':
                pygame.mixer.music.load("./audio/dah.ogg")
                pygame.mixer.music.play(loops=0)
            elif c == ' ':
                sleep(0.6)
            sleep(0.4)

    def show(self):
        print(f'> Here is the code:\n'
              f'{self.code.replace(".", "█ ").replace("-", "███ ")}')

    def encode(self):
        self.code = ''
        for c in self.text.lower():
            try:
                self.code += self.codes[c] + ' '
            except KeyError:
                continue
