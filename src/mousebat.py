from _collections_abc import Callable
from pygame.math import Vector2 as Vector
from settings import *  # pylint: disable=wildcard-import,unused-wildcard-import
from drawing_tools import WorldObject

class MouseBat(WorldObject):
    def __init__(self):
        super().__init__(0)
        self.pos = Vector()
        pygame.mouse.set_visible(False)
        self.radius = 20

    def refresh(
        self,
        delta_time: float,
        scaler_func: Callable[[Vector], Vector],
        destination_surface: pygame.surface.Surface,
    ):  # pylint: disable=missing-function-docstring
        self.input()
        self.draw(destination_surface)

    def input(self):
        self.pos = pygame.mouse.get_pos()

    def draw(self, destination_surface: pygame.surface.Surface):

        image = pygame.surface.Surface(
            (2 * self.radius + 2, 2 * self.radius + 2), pygame.SRCALPHA
        )
        pygame.draw.circle(
            image, "yellow", (self.radius + 1, self.radius + 1), self.radius
        )
        self.collision_mask = pygame.mask.from_surface(image)
        self.rect = (self.pos[0], self.pos[1], image.width, image.height)
        #image = self.collision_mask.to_surface(setcolor='red', unsetcolor='green')
        destination_surface.blit(image, self.rect)
