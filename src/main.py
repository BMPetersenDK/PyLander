"""
Main entry point of the game.
"""

import logging
from settings import *  # pylint: disable=wildcard-import
from drawing_tools import XYtoScreen, WorldObject
from rocket import Rocket
from mousebat import MouseBat
from typing import List


class Game:
    """
    Main game class.
    """

    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.Clock()
        self.font = pygame.font.Font()

        self.all_objects = []

        #
        # Setup the mapping from game coordinates to screeen coordinates.
        #
        self.scaler = XYtoScreen(WINDOW_WIDTH, WINDOW_HEIGHT, (-100, 0), 2)

    def run(self):
        """
        run Run the game
        """
        logging.info("Starting Game.run()")

        #
        # Add objects to the game
        #
        self.all_objects.append(Rocket())
        self.all_objects.append(MouseBat())

        # If the game should quit, the flag is set to true
        # and the game loop should be exited.
        quitting: bool

        quitting = False

        while quitting is False:
            delta_time = self.clock.tick(500) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitting = True
                    logging.info("Pygame QUIT event captured. quitting.")

            if quitting is False:
                #
                # Update all objects and append the resulting drawing commands
                #
                self.display_surface.fill('Black')
                for obj in self.all_objects:
                    obj.refresh(delta_time ,self.scaler, self.display_surface)
                #
                # Do collision checks
                #
                #
                coliding_objects: List[WorldObject]
                coliding_objects = [obj for obj in self.all_objects if obj.collision_mask is not None ]
                for i in range(len(coliding_objects)-1):
                    for j in range(i+1,len(coliding_objects)):
                        i_pos = (coliding_objects[i].rect[0],coliding_objects[i].rect[1])
                        j_pos = (coliding_objects[j].rect[0],coliding_objects[j].rect[1])
                        offset = (i_pos[0] - j_pos[0], i_pos[1] - j_pos[1])
                        if coliding_objects[i].rect.colliderect(coliding_objects[j].rect) is True:

                            collision = coliding_objects[i].collision_mask.overlap(
                                 coliding_objects[j].collision_mask,
                                (coliding_objects[j].rect[0] - coliding_objects[i].rect[0],
                                 coliding_objects[j].rect[1] - coliding_objects[i].rect[1])
                                )
                            if  collision is not None:
                                print(f"{self.clock} Collision!")
                                coliding_objects[i].collision(coliding_objects[j])
                                coliding_objects[j].collision(coliding_objects[i])

                pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    # The purpose here is to setup infrastructure for the game
    # and instaiate a Game
    logging.basicConfig(
        filename="logs/app.log",
        encoding="utf-8",
        filemode="w",
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )
    Game().run()
