# pylint: disable=missing-module-docstring

from pygame.math import Vector2 as Vector
from settings import *  # pylint: disable=wildcard-import,unused-wildcard-import


class Rocket:
    """
    Rocket Class represents a rocket that can move around
    """

    def __init__(self):  # pylint: disable=missing-function-docstring

        self.shape = (
            Vector(0.0, 0.0),
            Vector(5.00, 10.0),
            Vector(10.0, 0.0),
            Vector(5.0, 2.5),
        )

        self.pos = Vector(0.0, 0.0)
        self.shape_origin_to_image_center = Vector(0.0, 0.0)
        self.velocity = Vector(0.0, 0.0)

        self.angle = 0.0
        self.angular_velocity = 0.0

    def refresh(self, blit_queue, delta_time: float, scaler_func ):  # pylint: disable=missing-function-docstring
        self.input(delta_time)
        self.draw(blit_queue, scaler_func)
        self.print_info(blit_queue)

    def print_info(self, blit_queue):  # pylint: disable=missing-function-docstring
        font = pygame.font.Font()
        blit_queue.add(
            font.render(
                f"rocket:\n"
                f"Position: {self.pos}\n"
                f"Velocity: {self.velocity}\n"
                f"Angle: {self.angle}\n"
                f"Angular velocity: {self.angular_velocity}\n",
                True,  # antialias
                "white",
            ),  # color
            (0, 0),
            100,
        )

    def input(self, delta_time: float):  # pylint: disable=missing-function-docstring
        """
        input _summary_

        Parameters
        ----------
        delta_time : float
            _description_
        """
        rotation_factor = 20
        left_right_factor = 20
        up_down_factor = 20

        keys = pygame.key.get_pressed()

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

        self.angle = (self.angle + self.angular_velocity * delta_time) % 360
        self.pos += self.velocity

    def draw(
        self, blit_queue, scaler_func ):  # pylint: disable=missing-function-docstring
        """
        draw _summary_

        Parameters
        ----------
        blit_queue : _type_
            _description_
        x_scaler : _type_
            _description_
        y_scaler : _type_
            _description_
        """

        rotated_shape = [v.rotate(self.angle) for v in self.shape]

        # build new image for the rotated shape
        x_min = min(x for (x, y) in rotated_shape)
        x_max = max(x for (x, y) in rotated_shape)
        y_min = min(y for (x, y) in rotated_shape)
        y_max = max(y for (x, y) in rotated_shape)

        image = pygame.Surface((x_max - x_min, y_max - y_min))
        image.fill("grey")
        pygame.draw.polygon(image, "red", rotated_shape)
        blit_queue.add(image, scaler_func( (100,100) ))
