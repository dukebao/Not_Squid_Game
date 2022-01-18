from .base import PygameView
import pygame

FILEPATH = 'data/menu/'

class MenuView(PygameView):
    """ View Menu selection """

    def __init__(self,view):
        super().__init__(view)
        self.difficulty = None
        self.select_pos = [150,355]

    def draw(self):
        squid_pink = (244,71,136)
        self.window.fill((255, 255, 255))
        gamelogo = pygame.image.load(FILEPATH+'Gamelogo.png')
        self.window.blit(gamelogo,(10,10))

        self.easy_button = pygame.draw.circle(self.window,squid_pink,[100,200],80)
        pygame.draw.circle(self.window,(255,255,255),[100,200],40)

        self.medium_button = pygame.draw.polygon(surface=self.window, color=squid_pink, points=[(270,120), (200,280), (340,280)])
        pygame.draw.polygon(surface=self.window, color=(255,255,255), points=[(270,170), (240,260), (300,260)])
 
        self.hard_button = pygame.draw.rect(self.window,squid_pink,(380,140,140,140))
        pygame.draw.rect(self.window,(255,255,255),(415,175,70,70))

        self.start_button = self.render_text_surface('Start Game')
        self.window.blit(self.start_button,(200,350))

        self.control_button = self.render_text_surface('Control')
        self.window.blit(self.control_button,(200,380))

        self.info_button = self.render_text_surface('Information')
        self.window.blit(self.info_button,(200,410))

        #draw selection icon
        self.selecticon= pygame.image.load(FILEPATH+'icon.png')
        selecticonpos = (self.select_pos[0],self.select_pos[1])
        self.window.blit(self.selecticon,selecticonpos)


class GameMenuView(PygameView):
    """ View difficulty selection """

    def __init__(self,view):
        super().__init__(view)
        self.difficulty = None
        self.select_pos = [150,355]

    def draw(self):
        squid_pink = (244,71,136)
        self.window.fill((255, 255, 255))
        gamelogo = pygame.image.load(FILEPATH+'Gamelogo.png')
        self.window.blit(gamelogo,(10,10))

        self.start_button = self.render_text_surface('Level 1')
        self.window.blit(self.start_button,(200,350))

        self.control_button = self.render_text_surface('Level 2')
        self.window.blit(self.control_button,(200,380))

        self.info_button = self.render_text_surface('Level 3')
        self.window.blit(self.info_button,(200,410))

        self.info_button = self.render_text_surface('Level 4')
        self.window.blit(self.info_button,(200,440))

        #draw selection icon
        self.selecticon= pygame.image.load(FILEPATH+'icon.png')
        selecticonpos = (self.select_pos[0],self.select_pos[1])
        self.window.blit(self.selecticon,selecticonpos)
