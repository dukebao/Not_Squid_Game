from models.level1 import Shooter
from .base import PygameView
import pygame
from models import Enemy,Player
class Level1View(PygameView):
    """Render the First Level """

    def __init__(self,view):
        super().__init__(view)
        # self.character = pygame.image.load('bob.png')
        self.player = Player([50,250])
        a = Enemy([50,50],ms=300)
        b = Enemy([50,150],ms=350)
        c = Enemy([50,350],ms=200)
        d = Enemy([50,450],ms=150)
        
        self.s1 = Shooter([1150,150])
        self.s2 = Shooter([1150,350])
        # s3 = Shooter(s2)
        self.enemylist = [a,b,c,d]
        self.a = a 
        self.b = b
        self.c = c 
        self.d = d 
        #each round is 5 seconds for now 
        self.round_time = 5 

        self.doll = pygame.image.load('doll.png')
        self.shooter = pygame.image.load('shooter.png')
        self.character_pos=[50,350]
    

    def draw(self):

        self.window.fill((255,255,255))
        self.window.blit(self.player.display,(self.player.x,self.player.y))

        self.window.blit(self.a.display,((self.a.x,self.a.y)))
        self.window.blit(self.b.display,((self.b.x,self.b.y)))
        self.window.blit(self.c.display,((self.c.x,self.c.y)))
        self.window.blit(self.d.display,((self.d.x,self.d.y)))
        self.window.blit(self.s1.display,((self.s1.x,self.s1.y)))
        # self.window.blit(self.s2.display,((self.s2.x,self.s2.y)))
        self.window.blit(self.s1.bullet,((self.s1.bullet_x,self.s1.bullet_y)))
        
        # self.window.blit(self.doll,((400,200)))
        # self.window.blit(self.shooter,((400,250)))
        # self.window.blit(self.shooter,((100,150)))



