"""
Tools for facilitating drawing
"""
from typing import Tuple
import math
import pygame

class XYScaler():
    """
    Scaler perform a mapping from one linear scale to an other linear scale.

    The mapping is made so a/b equals a_prime / b_prime
                  +---- b ----------------------+
                  +---- a -----+                |
                  x1           v                x2
        ----------+------------+----------------+------>>
                  x1_prime     v_prime          x2_prime
                  +- a_prime --+                |
                  +- b_prime--------------------+

    a/b = = a_prime / b_prime
    (v-x1) / ( x2- x1 ) = (v_prime - x1_prime) / ( x2_prime - x1_prime )

    rearragning terms gives:
    v_prime = (v - x1)*(x2_prime - x1_prime)/(x2 - x1) + x1_prime

    we let scaler_factor = (x2_prime - x1_prime)/(x2 - x1):
    v_prime = (v - x1)*scale_factor + x1_prime

    To simplyfy calculations , x1,x2 x1_prime and x2_prime is given to the constructor.
    This way we an also avoid computing the scale_factor for every mapping.
    """
    def __init__(self, p1a, p1b, p2a, p2b, aspect_locked = False):
        """
        __init__  Setup the scaling by supplying 2 points coordinates values in each.

        Parameters
        ----------
        p1a : tuple[float,float]
            Point 1 in the source system.

        p1b : tuple[float,float]
            Point 1 in the destination system.

        p2a : tuple[float,float]
            Point 2 in the source system.

        p2b : tuple[float,float]
            Point 2 in the destination system

        aspect_locked : bool, optional
            If true the scaling from the first axis will be used on all coordinates.
            By default False

        Raises
        ------
        ValueError
            If coordinates are so close that scaling factor can be determined.
        """
        self.p1a = p1a
        self.p1b = p1b

        if math.isclose(p1a[0], p2a[0]):
            raise ValueError("p1a[0] and p2a[0] are too close.")
        if math.isclose(p1a[1], p2a[1]):
            raise ValueError("p1a[1] and p2a[1] are too close.")
        if math.isclose(p1b[0], p2b[0]):
            raise ValueError("p1b[0] and p2b[0] are too close.")
        if math.isclose(p1b[1], p2b[1]):
            raise ValueError("p1b[1] and p2b[1] are too close.")

        if aspect_locked is True:
            self.factor = (
                       float( p2b[0] - p1b[0] ) / float( p2a[0] - p1a[0]),
                       float( p2b[0] - p1b[0] ) / float( p2a[0] - p1a[0])
                       )
        else:
            self.factor = (
                       float( p2b[0] - p1b[0] ) / float( p2a[0] - p1a[0]),
                       float( p2b[1] - p1b[1] ) / float( p2a[1] - p1a[1])
                       )

    def __call__(self, val):
        """
        __call__ Setup the scaling.

        Parameters
        ----------
        val : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        return (
                (val[0]-self.p1a[0])*self.factor[0]+self.p1b[0],
                (val[1]-self.p1a[1])*self.factor[1]+self.p1b[1]
                )


class BlitQueue():
    """
    BlitQueue A convinience class built to handle z ordering surfaces
    before feeding them to blit operation.

    Surfaces are added with the add() method, and retieved order by z_alue by get()
    """
    def __init__(self):
        """
        __init__ Initialize the queue
        """
        self._queue=[]

    def add(self, surface: pygame.surface, position: Tuple[int,int] = (0,0), z_order:int = 0) :
        """
        add Adds a surface tor the queue

        Parameters
        ----------
        surface : pygame.surface
            Surface to be added to the queue

        position : Tuple[int,int]
            Position the surface sould be blitted into the destination surface given as (x,y)

        z_order : int
            The sorting order. When retieved the queue is stored in ascending z_order
        """
        self._queue.append( (surface, position, z_order) )

    def get(self):
        """
        get Return a list of surfaces sorted in with z ascending.

        Returns
        -------
        A list suitable to pass to a pygame.surface.fblits() call_
        """
        return [(surface, pos) for (surface, pos, z_order)
                in sorted(self._queue, key=lambda e: e[2])]

    def clear(self):
        """
        clear Clears the queue
        """
        self._queue=[]
