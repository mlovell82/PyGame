#space_rocks/game.py
import pygame
from utils import load_sprite

class SpaceRocks:
    def __init__(self):
        #Initialize pygame and set the title
        pygame.init()
        pygame.display.set_caption("Space Rocks")

        self.screen = pygame.display.set_mode((800,600))
        self.background = load_sprite("space", False)

    def main_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._drawRectangle()
            self._draw()
            #self._drawRectangle()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def _game_logic(self):
        pass

    def _draw(self):
        self.screen.blit(self.background,(0,0))
        pygame.display.flip()

    def _drawRectangle(self):
        pygame.draw.rect(self.screen,(255,192,203),pygame.Rect(30,30,60,60))
        pygame.display.flip()
