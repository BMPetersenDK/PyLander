import logging
from settings import * #pylint: disable=wildcard-import


class Game:
    """
    Main game class.
    """
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.clock = pygame.Clock()
        self.font = pygame.font.Font()

        #
        #( (surface, destination), z_order}
        #

        self.fblits_surfaces = []

    def run(self):
        """
        run Run the game
        """
        logging.info("Starting Game.run()")
        quitting = False
        while quitting is False:
            delta_time = self.clock.tick(500)/1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitting = True
                    logging.info("Pygame QUIT event captured. quitting.")

            #
            # Render hello world
            #
            message_surf = self.font.render('Hello \nworld!',True,'white')


            if quitting is False:
                self.display_surface.fill('grey')
                self.fblits_surfaces.append(
                    ( (message_surf,self.display_surface.get_rect().center),0)
                    )


                self.fblits_surfaces.sort(key = lambda e: e[1])
                self.display_surface.fblits(self.fblits_surfaces)
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