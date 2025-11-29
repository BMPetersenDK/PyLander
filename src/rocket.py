#pylint: disable=missing-module-docstring

# import logging
from pygame.math import Vector2 as Vector
from moveable_object import MoveableObject
from settings import * #pylint: disable=wildcard-import,unused-wildcard-import

class Rocket(MoveableObject):
    """
    Rocket Class represents a rocket that can move around
    """
    def __init__(self):
        super().__init__(
            Vector(200.0,200.0),
            0.0,
            (Vector( -50.0,  -40.0),
             Vector(0.00,  60.0),
             Vector(50.0, -40.0),
             Vector( 0.0, -15.0)
             )
            )

    def draw(self):
        """
        draw Draws the rocket on pygame surface

        Raises:
            ValueError: If pygame does not return a surface to draw on
        """
        screen = pygame.display.get_surface()
        if screen is None:
            raise ValueError("Surface not found.")
        pygame.draw.polygon(screen,'red',self.transform_shape(),2)
