"""
Tools for facilitating drawing
"""

from collections.abc import Callable
from enum import Enum, auto
from pygame import Vector2 as Vector
import pygame


class XYtoScreen:
    """
    A Callable class which maps game coordinate system to screen coordinates.
    """

    def __call__(self, p):
        return (
            (p[0] - self.bottomleft[0]) * self.pixels_per_unit,
            self.window_height - (p[1] - self.bottomleft[1]) * self.pixels_per_unit,
        )

    def __init__(
        self,
        window_width: int,
        window_height: int,
        bottomleft: Vector,
        pixels_per_unit: float,
    ):
        self.bottomleft = bottomleft
        self.pixels_per_unit = pixels_per_unit
        self.window_width = window_width
        self.window_height = window_height
        self.topright = self.bottomleft + (
            float(self.window_width) / float(self.pixels_per_unit),
            float(self.window_height) / float(self.pixels_per_unit),
        )


class CoordinateSystem(Enum):
    """ENUm to identify what coordinate system a vector belongs to."""

    GAME = auto()
    SCREEN = auto()


class NamedReferencePoint(Enum):
    """Enum to reference positions in a rectangle / screen / window"""

    TOPLEFT = auto()
    BOTTOMLEFT = auto()
    TOPRIGHT = auto()
    BOTTOMRIGHT = auto()
    CENTER = auto()

class WorldObject:
    def __init__(self, z):
        self.z:int = z
        self.rect: pygame.rect.Rect = None
        self.collision_mask: pygame.mask.Mask = None

    def refresh(
        self,
        delta_time: float,
        scaler_func: Callable[[Vector], Vector],
        destination_surface: pygame.surface.Surface,
    ):
        raise NotImplementedError()

    def collision(self, collider: 'WorldObject'):
        pass
