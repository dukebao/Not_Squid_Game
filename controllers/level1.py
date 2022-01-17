from logging import FATAL
import pygame.locals

from models.level1 import Enemy,Target
from .base import PygameController
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN
import random
from pydub import AudioSegment
from models import speed_changer
import os
from models import Projectile

class Level1Controller(PygameController):
    """controler for level 1"""

    FPS = 60
    file_path = 'squid-game-doll.wav'
    pygame.mixer.init()
    # a = pygame.mixer.Sound('mymusic.ogg')

    def __init__(self,view):
        """constroctor - set variables """

        super().__init__(view)
        self.player = self.view.player
        self.a = self.view.a
        self.b = self.view.b
        self.c = self.view.c
        self.d = self.view.d
        self.bullet1 = self.view.bullet1
        self.a_target = random.randint(0,450)
        self.b_target = random.randint(0,500)
        self.c_target = random.randint(0,500)
        self.d_target = random.randint(0,500)
        self.sound = pygame.mixer.Sound('squid-game-doll.wav')
        self.scan = pygame.mixer.Sound('scan.wav')

        self.s1 = self.view.s1
        self.s2 = self.view.s2

        round_end = pygame.USEREVENT + 1
        scan_end = pygame.USEREVENT + 2
        self.round_end = pygame.mixer.Channel(0).set_endevent(round_end)
        self.scan_end = pygame.mixer.Channel(1).set_endevent(scan_end)

        self.targets = []

    def change_tempo(self,filepath='squid-game-doll.wav',newSpeed=1.2):
        mysound = 'fast.wav'
        sound = AudioSegment.from_file(filepath)    
        speed_sound=speed_changer(sound,newSpeed)
        speed_sound.export(os.path.join(mysound),format='wav')
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(mysound)
        
        return mysound

    def process(self,event):
        running = super().process(event)
        # target = random.randint(0,500)
       
        if running is False:
            return False

        if event.type== KEYDOWN and event.key == pygame.locals.K_ESCAPE:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == pygame.locals.K_UP:
                self.player.y -= 10
            elif event.key == pygame.locals.K_DOWN:
                self.player.y += 10
            elif event.key == pygame.locals.K_RIGHT:
                self.player.x += 10
            elif event.key == pygame.locals.K_LEFT:
                self.player.x -= 10
        if event.type == MOUSEBUTTONDOWN:
            print(event.pos)
        return True

    def run(self,stop_after = None):
        count = 0 
        round_end = 0
        running = True
        start = pygame.time.get_ticks()
        clock = pygame.time.Clock()

        objestlist = [self.a,self.b,self.c,self.d,self.player]
        
        round_restart = 4000

        pygame.mixer.Channel(0).play(self.sound)
        mysound = self.change_tempo()

        while running is True:
            music_off = pygame.mixer.Channel(0).get_busy()
            clock.tick(self.FPS)
            self.view.draw()
            self.view.update()
    
            if pygame.mixer.Channel(0).get_busy():
                start_time = pygame.time.get_ticks() + round_restart
            else:
                if pygame.time.get_ticks() > start_time:
                    pygame.mixer.Channel(0).play(self.sound)
                    mysound = self.change_tempo(mysound)
                    if round_end == count:
                        round_end = round_end + 1
                    count = count + 1 
                       

            if count > 5 or self.player.alive is False:
                print('you lost')
                running = False
            
            if self.player.x > 1100:
                print('you win')
                running = False
        
            for event in pygame.event.get():
                running = self.process(event)

            now = pygame.time.get_ticks()
            if stop_after is not None:
                if now - start >= stop_after* 1000:
                    running = False
        

            #this block of code controls cpu movement
            elaspe = start_time - pygame.time.get_ticks()
            if music_off:
                if self.a.reach_target((1100,self.a_target)) is False and self.a.alive:
                    self.a.moveto((1100,self.a_target))
                if self.b.reach_target((1100,self.b_target)) is False and self.b.alive:
                    self.b.moveto((1100,self.b_target))
                if self.c.reach_target((1100,self.c_target)) is False and self.c.alive:
                    self.c.moveto((1100,self.c_target))
                if self.d.reach_target((1100,self.d_target)) is False and self.d.alive:
                    self.d.moveto((1100,self.d_target))
            
            if elaspe < 3900 and elaspe > 2500:
                self.s1.moveto((1000,150))
                self.s2.moveto((1000,350))
                self.bullet1.x = self.s1.x
                self.bullet1.y = self.s1.y
            elif elaspe < 1500 and elaspe > 0:
                self.s1.moveto((1150,150))
                self.s2.moveto((1150,350))
                self.bullet1.x = self.s1.x
                self.bullet1.y = self.s1.y
            
            
            #save player location into a list 
            if elaspe < 3980 and elaspe > 3950:
                print('recording location')
                self.targets.append([self.player.x,self.player.y])
    
            if round_end == count:
                if elaspe < 2000 and elaspe > 0:
                    if self.player.alive:
                        current_pos = [self.player.x,self.player.y]
                        if current_pos not in self.targets:
                            self.bullet1.shoot_status = True 
                            round_end = round_end + 1

            if self.bullet1.shoot_status:
                if not self.bullet1.shoot((self.player.x,self.player.y)):
                    self.bullet1.shoot((self.player.x,self.player.y))
                else :
                    self.bullet1.shoot_status = False

            # print(self.bullet1.hitbox)
            for item in objestlist:
                if self.bullet1.check_hit(item):
                    item.alive = False
     
            self.bullet1.update_pos()
            for item in objestlist:
                item.update_pos()
            # print(self.player.hitbox)
            # print(self.a.hitbox)
            
            