import pygame, sys
from pygame.locals import *
from player import Player
from start import Start
from game import Game

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Manager:
    def __init__(self, width, height):
        self.width, self.height = width, height
        pygame.init()
        # self.states = {"start": Start(self), "game": Game(self)}
        self.states = {"start": Start(self), "game": None}

        self.current_state = "start"

        #self.woah = False


    def loop(self):
        while True:
            self.states[self.current_state].loop()
            print(self.current_state)
