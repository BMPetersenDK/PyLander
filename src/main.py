"""
Main entry point of the game.
"""
import logging
from rocket import Rocket
from settings import * #pylint: disable=wildcard-import



class Game:
    """
    Main game class. 
    """
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.rocket = Rocket()

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
            self.display_surface.fill('black')
            self.rocket.rotate(0.1)
            self.rocket.draw()
            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    # The purpose here is to setup infrastructure for the game
    # and instaiate a Game
    logging.basicConfig(
        filename="logs/app.log",
        encoding="utf-8",
        filemode="w",
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
        )
    Game().run()
