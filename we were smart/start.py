import pygame, sys
from pygame.locals import *
import config
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)
class Start():
    def __init__(self, manager):
        # pygame.init()
        #Set up the window
        self.manager = manager
        self.windowSurface = pygame.display.set_mode((config.WIDTH, config.HEIGHT), 0 , 32)
        pygame.display.set_caption('Start')

        #Set up the colors
        BLACK = (0,0,0)
        RED = (255,0,0)
        GREEN = (0,255,0)
        BLUE = (0,0,255)
        WHITE = (255,255,255)

        #Set up fonts
        basicFont = pygame.font.SysFont(None, 48)

        #Set up the text
        text = basicFont.render('WELCOME TO OUR GAME!', True, BLACK)
        textRect = text.get_rect()
        textRect.centerx = self.windowSurface.get_rect().centerx
        textRect.centery = self.windowSurface.get_rect().centery - 150

        #Draw the white background onto the surface
        self.windowSurface.fill(WHITE)

        # #Draw a blue poligon onto the surface
        # pygame.draw.polygon(windowSurface, BLUE, ((250, 0), (500,200),(250,400), (0,200) ))

        # #Draw a green poligon onto the surface
        # pygame.draw.polygon(windowSurface, GREEN, ((125,100),(375,100),(375,300),(125,300)))

        # #Draw a red circle onto the surface
        # pygame.draw.circle(windowSurface, RED, (250,200), 125)

        #Draw the text onto the surface
        self.windowSurface.blit(text,textRect)

        #Draw the window onto the screen
        pygame.display.update()

        # player = Player()
        
        #windowSurface.blit(player.surf, (self.width/2, self.height/2))
        pygame.display.flip()

        #Run the game loop

    def loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == MOUSEBUTTONDOWN:
            #    self.manager.current_state = "game"

            # pressed_keys = pygame.key.get_pressed()
            # player.update(pressed_keys)