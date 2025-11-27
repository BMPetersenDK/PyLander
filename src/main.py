"""
Main entry point of the game.
"""
from settings import * #pylint: disable=wildcard-import

class Game:
    """
    Main game class. 
    """
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    def run(self):
        """
        run Run the game
        """
        quitting = False
        while quitting is not True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitting = True
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
