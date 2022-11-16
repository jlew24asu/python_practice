""" Some practice at python building a game


Jeff built this game. its available for purchase $1,000,000,000.01


"""


import sys
import pygame
from settings import Settings

class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        
        """old settings prior to making settings.py class"""
        #self.screen = pygame.display.set_mode((1200, 800))
        #pygame.display.set_caption("Alien Invasion")
        #self.bg_color = (230,230,230)
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
       
        
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
     
     
     
     
     
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()