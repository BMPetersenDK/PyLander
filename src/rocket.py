# pylint: disable=missing-module-docstring

from _collections_abc import Callable
from pygame.math import Vector2 as Vector
from settings import *  # pylint: disable=wildcard-import,unused-wildcard-import
from drawing_tools import WorldObject

class Rocket(WorldObject):
    """
    Rocket Class represents a rocket that can move around
    """

    def __init__(self):  # pylint: disable=missing-function-docstring
        super().__init__(0)
        self.shape = (
            Vector(-50.0, -40.0),
            Vector(  0.0,  60.0),
            Vector( 50.0, -40.0),
            Vector(  0.0, -15.0),
        )

        self.pos = Vector(0.0, 0.0)
        self.shape_origin_to_image_center = Vector(0.0, 0.0)
        self.velocity = Vector(0.0, 0.0)
        self.collision_flag = False
        self.angle = 0.0
        self.angular_velocity = 0.0

    def refresh(
        self,
        delta_time: float,
        scaler_func: Callable[[Vector], Vector],
        destination_surface: pygame.surface.Surface,
    ):  # pylint: disable=missing-function-docstring
        self.input(delta_time)
        self.draw(scaler_func, destination_surface)
        self.print_info(destination_surface, scaler_func)
        self.collision_flag = False

    def print_info(
        self, destination_surface, scaler_func
    ):  # pylint: disable=missing-function-docstring
        font = pygame.font.Font()
        destination_surface.blit(
            font.render(
                f"rocket:\n"
                f"Game Position: {self.pos}\n"
                f"Screen position: {scaler_func(self.pos)}\n"
                f"Rect: {self.rect}\n"
                f"Velocity: {self.velocity}\n"
                f"Angle: {self.angle}\n"
                f"Angular velocity: {self.angular_velocity}\n"
                f"Centroid: {self.collision_mask.centroid()}",
                True,  # antialias
                "white",
            )
        )
    def collision(self, collider):
        self.collision_flag = True

    def input(self, delta_time: float):  # pylint: disable=missing-function-docstring
        """
        input _summary_

        Parameters
        ----------
        delta_time : float
            _description_
        """
        rotation_factor = 20
        left_right_factor = 2
        up_down_factor = 2

        keys = pygame.key.get_pressed()

        self.velocity *= 0.99999

        if keys[pygame.K_d]:
            self.velocity.x += left_right_factor * delta_time
        if keys[pygame.K_a]:
            self.velocity.x -= left_right_factor * delta_time
        if keys[pygame.K_w]:
            self.velocity.y += up_down_factor * delta_time
        if keys[pygame.K_s]:
            self.velocity.y -= up_down_factor * delta_time
        if keys[pygame.K_LEFT]:
            self.angular_velocity += rotation_factor * delta_time
        if keys[pygame.K_RIGHT]:
            self.angular_velocity -= rotation_factor * delta_time
        if keys[pygame.K_SPACE]:
            self.angular_velocity = 0
            self.velocity = Vector()
        self.angle = (self.angle + self.angular_velocity * delta_time) % 360
        self.pos += self.velocity

    def draw(self, scaler_func, destination_surface: pygame.surface.Surface):

        shape = [scaler_func(v.rotate(self.angle)) +self.pos for v in self.shape]

        # build new image for the rotated shape
        x_min = min(x for (x, y) in shape)
        x_max = max(x for (x, y) in shape)
        y_min = min(y for (x, y) in shape)
        y_max = max(y for (x, y) in shape)

        # We draw the shape onto a surface that we later will blit into
        # the destination based on the topleft corner.
        # Therefore we need to draw the coordinates relative to the topleft corner
        shape = [(x-x_min, y-y_min) for (x,y) in shape]
        self.rect = pygame.rect.FRect(x_min, y_min, x_max-x_min, y_max-y_min)

        self.surface = pygame.Surface(
            (self.rect.width, self.rect.height), pygame.SRCALPHA )
        # self.surface.fill("grey")
        if self.collision_flag is True:
            color = 'red'
        else:
            color = 'green'

        pygame.draw.polygon(self.surface, color, shape)
        self.collision_mask = pygame.mask.from_surface(self.surface)
        pygame.draw.circle(self.surface, 'yellow',self.collision_mask.centroid(),4)
        pygame.draw.circle(self.surface, "blue", scaler_func( (0,0) ), 4)
        destination_surface.blit(self.surface, self.rect)
