"""
Main entry point of the game.
"""
import logging

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
        logging.info("Starting Game.run()")
        quitting = False
        while quitting is not True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitting = True
                    logging.info("Pygame QUIT event captured. quitting.")
            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    logging.basicConfig(
        filename="logs/app.log",
        encoding="utf-8",
        filemode="w",
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
        )
    game = Game()
    game.run()
