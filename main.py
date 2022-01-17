import pygame
from controllers import GameMenuController, MenuController,GameInstructionController,Level1Controller
from views import MenuView,GameMenuView,GameInstructionView,Level1View


def main():
    """Main Program"""
    pygame.init()
    window = pygame.display.set_mode((600,500))
    
    window = pygame.display.set_mode((1200,500))

    level1_view = Level1View(window)
    level1 = Level1Controller(level1_view)
    level1.run()



    # """this pieces of code are working code"""
    # menu_view = MenuView(window)

    # main_menu = MenuController(menu_view)

    # main_menu.run(stop_after=10)

    # if main_menu.selection == 'Start Game':
    #     print(main_menu.selection)
    #     game_menu_view = GameMenuView(window)
    #     game_menu = GameMenuController(game_menu_view)
    #     game_menu.run(stop_after=120)

    #     if game_menu.selection == 'Level 1':
    #         print(game_menu.selection)
    #     elif game_menu.selection == 'Level 2': 
    #         print(game_menu.selection)
    #     elif game_menu.selection == 'Level 3': 
    #         print(game_menu.selection)
    #     elif game_menu.selection == 'Level 4': 
    #         print(game_menu.selection)

    # elif main_menu.selection == 'Information':
    #     print(main_menu.selection)
    # elif main_menu.selection == 'Control':
    #     print(main_menu.selection)

    

if __name__ == "__main__":
    main()