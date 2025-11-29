#pylint: disable=missing-module-docstring

from pygame.math import Vector2 as Vector

class MoveableObject:
    """
     MoveableObject holds values and functions to move objects around in the
     game world and transform thier coordinates to screen coordinates
    """
    def __init__(self,position:Vector, angle: float, shape: tuple[Vector]):
        """Init the calsse with the values given"""
        self.position(position)
        self.angle(angle)
        self.shape = shape

    def angle(self, new_angle:float = None):
        """
        Set the rotation angle for the object if a vlue is passed.
        Returns the current rotation
        """
        if new_angle is not None:
            self.current_angle = new_angle
        return self.current_angle

    def rotate(self, rotation:float):
        """
        Change the angle with the given amount.
        """
        self.current_angle += rotation

    def position(self, new_position:Vector = None):
        """
        sets the position vecto to a new value. if a value is given.
        Returns the current position vector."""
        if new_position is not None:
            self.current_position = new_position
        return self.current_position

    def move(self, movement:Vector):
        """Change the position vector by adding the movement Vector to it"""
        self.current_position += movement

    def transform_shape(self):
        """
        perform the following transformations in order:
        1) Rotate the shape
        2) Move the shape to its position
        """
        return tuple(v.rotate(self.current_angle)+self.current_position for v in self.shape)
