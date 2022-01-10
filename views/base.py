from abc import ABC,abstractmethod

import pygame
import pygame.font

class PygameView(ABC):
    """abstract class for basic pygame view"""

    def __init__(self,window):
        """constructor received a window (where image is being rendered) 
        
        - methods - render_text_surface (string)
        renders text to window
        """
        self.window = window

    def render_text_surface(Self,text):
        """
        takes string to render as mendatory argument - text 
        optional arguments 
        color of the text : color , (0,0,0)

        """
        arial = pygame.font.SysFont("arial",24)
        text_surface = arial.render(text,True,(0,0,0))

        return text_surface

    @abstractmethod
    def draw(self):
        """ child class must implement the draw method """
        raise NotImplementedError

    def update(self):
        """update the"""
        pygame.display.flip()