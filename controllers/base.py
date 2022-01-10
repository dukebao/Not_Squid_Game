

from abc import ABC,abstractmethod

import pygame
import pygame.locals
import sys

class PygameController(ABC):
    """This classs defines a few basic controllers 
    
    Controllers inherit from this class are able to run a pygame loop 
    by calling the proper method

    Run method - runs pygame loop and pass the event to self.process which returns a bloon
    takes optional argument 'stop_after` -> defines maximum amount of time to run the loop for ( in seconds )


    process method - abstract method. 

    """
    FPS = 60
    def __init__(self,view):
        self.view = view

    def run(self,stop_after = None):
        running = True
        start = pygame.time.get_ticks()
        clock = pygame.time.Clock()

        while running is True:
            clock.tick(self.FPS)
            self.view.draw()
            self.view.update()

            for event in pygame.event.get():
                running = self.process(event)
            
            now = pygame.time.get_ticks()
            if stop_after is not None:
                if now - start >= stop_after * 1000:
                    running = False
    
    def process(self,event):
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
        return True