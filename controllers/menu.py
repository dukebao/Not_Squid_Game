import pygame.locals
from .base import PygameController
from pygame.constants import KEYDOWN

class MenuController(PygameController):
    """Control main menu """

    def __init__(self,view):
        """constructor - set variables """

        super().__init__(view)

        self.selection = 'Start Game'

    def process(self,event):

        running = super().process(event)
        # print(self.view.select_pos)
        if running is False:
            return False
        
        if event.type== KEYDOWN and event.key == pygame.locals.K_ESCAPE:
            pygame.quit()
            exit()
        

        #350,380,410
        if event.type == KEYDOWN and event.key == pygame.locals.K_UP:
            self.view.select_pos[1] -= 35
            if self.view.select_pos[1] < 350:
                self.view.select_pos[1] = 350
        elif event.type == KEYDOWN and event.key == pygame.locals.K_DOWN:
            self.view.select_pos[1] += 35
            if self.view.select_pos[1] > 410:
                self.view.select_pos[1] = 410

        #375,390,410
        if event.type == KEYDOWN and event.key == pygame.locals.K_RETURN:
            if self.view.select_pos[1] <= 355:
                self.selection = 'Start Game'
            elif self.view.select_pos[1] == 390:
                self.selection = 'Control'
            elif self.view.select_pos[1] == 410:
                self.selection = 'Information'
            return False

        return True


class GameMenuController(PygameController):
    """Control Game menu """

    def __init__(self,view):
        """constructor - set variables """

        super().__init__(view)

        self.selection = 'Level 1'

    def process(self,event):

        running = super().process(event)
        # print(self.view.select_pos)
        if running is False:
            return False
        
        if event.type== KEYDOWN and event.key == pygame.locals.K_ESCAPE:
            pygame.quit()
            exit()
        


        offset = 5
        #350,380,410
        if event.type == KEYDOWN and event.key == pygame.locals.K_UP:
            self.view.select_pos[1] -= 30
            if self.view.select_pos[1] <= 350+offset :
                self.view.select_pos[1] = 350+offset
        elif event.type == KEYDOWN and event.key == pygame.locals.K_DOWN:
            self.view.select_pos[1] += 30
            if self.view.select_pos[1] > 440+offset :
                self.view.select_pos[1] = 440+offset

        #350/380/410/440
        print(self.view.select_pos[1])

        if event.type == KEYDOWN and event.key == pygame.locals.K_RETURN:
            if self.view.select_pos[1] <= 355:
                self.selection = 'Level 1'
            elif self.view.select_pos[1] == 385:
                self.selection = 'Level 2'
            elif self.view.select_pos[1] == 415:
                self.selection = 'Level 3'
            elif self.view.select_pos[1] == 445:
                self.selection = 'Level 4'
            return False

        return True

