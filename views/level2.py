from models.level1 import Projectile, Shooter
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
        bullet1 = Projectile([1150,150])
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
        self.bullet1 = bullet1
        self.doll = pygame.image.load('doll.png')
        self.shooter = pygame.image.load('shooter.png')
        self.character_pos=[50,350]
    

    def draw(self):

        self.window.fill((255,255,255))
        
        self.window.blit(self.player.display,(self.player.x,self.player.y))
        for item in self.enemylist:
            if item.alive:
                self.window.blit(item.display,((item.x,item.y)))
            else :
                self.window.blit(item.display_dead,((item.x,item.y)))
        self.window.blit(self.s1.display,((self.s1.x,self.s1.y)))
        self.window.blit(self.bullet1.display,((self.bullet1.x,self.bullet1.y)))
        pygame.draw.lines(self.window,(255,0,0),False,[(1100,0),(1100,500)],width=2)
        # self.window.blit(self.doll,((400,200)))
        # self.window.blit(self.shooter,((400,250)))
        # self.window.blit(self.shooter,((100,150)))



