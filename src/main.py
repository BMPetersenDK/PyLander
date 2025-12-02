"""
Main entry point of the game.
"""
import logging
from settings import * #pylint: disable=wildcard-import
from drawing_tools import XYScaler, BlitQueue
from rocket import Rocket


class Game:
    """
    Main game class.
    """
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.clock = pygame.Clock()
        self.font = pygame.font.Font()
        self.blit_queue = BlitQueue()
        self.all_objects = []

        #
        # Setup the mapping from game coordinates to screeen coordinates.
        # These are done with the Scaler class. One is use for each axis
        #
        # In order not to distort the image, the scalefactor must have the same
        # absolute value. As the game coordinates increase when moving up, and
        # screen coordinates do the opposite the scaling factor is negative.
        #
        self.scaler = XYScaler( (0,0), (0, WINDOW_HEIGHT), (2000,1000), (WINDOW_WIDTH,0) )

    def run(self):
        """
        run Run the game
        """
        logging.info("Starting Game.run()")

        #
        # Add objects to the game
        #
        self.all_objects.append(Rocket())

        # If the game should quit, the flag is set to true
        # and the game loop should be exited.
        quitting: bool

        quitting = False

        while quitting is False:
            delta_time = self.clock.tick(500)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitting = True
                    logging.info("Pygame QUIT event captured. quitting.")


            if quitting is False:
                #
                # Reset the list of surfaces to blit to the display
                #
                self.blit_queue.clear()

                #
                # Update all objects
                #
                for obj in self.all_objects:
                    obj.refresh(self.blit_queue ,delta_time,self.scaler)

                #
                # Fill the display_surface with background color.
                # and the draw objects on the display surface
                # then display the surface
                #
                self.display_surface.fill('black')
                self.display_surface.fblits(self.blit_queue.get())
                pygame.display.flip()
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
        level=logging.DEBUG
        )
    Game().run()
