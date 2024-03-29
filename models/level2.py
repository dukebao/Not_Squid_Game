import pygame
import pydub
from pygame.locals import *

class Enemy:
    """creating the enemy instance
    takes a mandatory position argument
    movement speed is set to default 5 for level 1 enemy

    """
    def __init__(self,pos:list,ms=300):
        self._x = pos[0]
        self._y = pos[1]
        self.movement_speed = ms
        self.display = pygame.image.load('enemy.png')
        self.display_dead = pygame.image.load('enemy_dead.png')
        self.alive = True
        self.hitbox = self.display.get_rect(topleft = (self._x,self._y))

    def moveto(self,target:list):
        """give a target location expecting a touple x and y
        object will move towards that position in a straight line
        at the speed of it's movement speed
        """
        clock = pygame.time.Clock()
        ms_frame = clock.tick(300)
        #next point calculation
        #target x and y target[0],target[1]

        x_distance_difference = target[0] - self.x
        y_distance_difference = target[1] - self.y

        x_movement_ratio = x_distance_difference / (x_distance_difference+ y_distance_difference)
        y_movement_ratio = y_distance_difference /( x_distance_difference+y_distance_difference)

        move_per_frame = (self.movement_speed*ms_frame/1000)

        self.x = self.x + x_movement_ratio*move_per_frame
        self.y = self.y + y_movement_ratio*move_per_frame

    def update_pos(self):
        self.hitbox =  self.hitbox = self.display.get_rect(topleft = (self._x,self._y))

    def reach_target(self,target:list):
        if self.x > target[0]:
            return True
        else :
            return False

    def check_hit(self):
        #collide
        collide = False
        return collide

    @property
    def x (self):
        return self._x
    @property
    def y(self):
        return self._y

    @x.setter
    def x(self,value):
        if value >= 0 :
            self._x = value
        else:
            raise UserWarning

    @y.setter
    def y(self,value):
        if value >= 0 :
            self._y = value
        else:
            raise UserWarning

    def __str__(self):
        return f'({self.x},{self.y})'

class Shooter:
    def __init__(self,pos):
      self._x = pos[0]
      self._y = pos[1]
      self.display = pygame.image.load('shooter.png')
      self.movement_speed = 500
      self.alive = True
      self.bullet = pygame.image.load('bullet.png')
      self.bullet_vel = 5

    #   self.bullet_x = self.x
    #   self.bullet_y = self.y
    #   self.shoot_status = False
    #   self.hitbox = self.bullet.get_rect(topleft = (self.bullet_x,self.bullet_y))
    def moveto(self,target:list):
        """give a target location expecting a touple x and y
        object will move towards that position in a straight line
        at the speed of it's movement speed
        """
        clock = pygame.time.Clock()
        ms_frame = clock.tick(300)
        x_distance_difference = (target[0] - self.x)
        y_distance_difference = (target[1] - self.y)

        try :
            x_movement_ratio = x_distance_difference / (x_distance_difference+ y_distance_difference)
            y_movement_ratio = y_distance_difference /( x_distance_difference+y_distance_difference)
        except(ZeroDivisionError):
            x_movement_ratio = 0
            y_movement_ratio = 0
        move_per_frame = (self.movement_speed*ms_frame/1000)

        if x_distance_difference < 0 :
            self.x = self.x - x_movement_ratio*move_per_frame
        else :
            self.x = self.x + x_movement_ratio*move_per_frame
        self.y = self.y - y_movement_ratio*move_per_frame

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    @x.setter
    def x(self,value):
        self._x = value
    @y.setter
    def y(self,value):
        self._y = value

    def __str__(self):
        return f'({self.x},{self.y})'

class Player:
    def __init__(self,pos):
        self.ms = 1000
        self.display = self.display = pygame.image.load('bob.png')
        self._x = pos[0]
        self._y = pos[1]
        self.alive = True
        self.hitbox = self.display.get_rect(topleft = (self._x,self._y))
    def check_hit(self,object):

        if abs(self.hitbox[0] - object.hitbox[0]) < self.hitbox[2] and abs(self.hitbox[1] - object.hitbox[1]) < self.hitbox[3]:
            return True
        else :
            return False

    def update_pos(self):
        self.hitbox =  self.hitbox = self.display.get_rect(topleft = (self._x,self._y))

    @property
    def x (self):
        return self._x
    @property
    def y(self):
        return self._y

    @x.setter
    def x(self,value):
        if value >= 0 :
            self._x = value
        else:
            raise UserWarning

    @y.setter
    def y(self,value):
        if value >= 0 :
            self._y = value
        else:
            raise UserWarning

    def __str__(self):
        return f'({self.x},{self.y})'

    """create player instance """
def main():
    a = Enemy((0,0))
    print(a)
    while a.reach_target((5,7)) is False :
        a.moveto((5,7))
        # print(a)
    b = Enemy((1,4))
    while b.reach_target((10,16)) is False:
        b.moveto((10,16))
    print(b)
    # print(a)
if __name__ == "__main__":
    main()