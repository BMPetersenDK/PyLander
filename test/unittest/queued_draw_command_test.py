"""
Unittests for drawing functions
"""

import pygame
from drawing_tools import (
    Polygon,
    Text,
    CoordinateSystem,
    NamedReferencePoint,
    XYtoScreen,
)
###################################################################################################
def assert_identical_surface(expected:pygame.surface.Surface,actual:pygame.surface.Surface):

    assert expected.width  == actual.width
    assert expected.height == actual.height

    expected_pixels = pygame.PixelArray(expected)
    actual_pixels = pygame.PixelArray(actual)

    for x in range(expected.width):
        for y in range(expected.height):
            assert actual_pixels[x, y] == expected_pixels[x, y]

###################################################################################################
def assert_identical_mask(expected_mask: pygame.mask.Mask, actual_mask:pygame.mask.Mask):
    assert expected_mask.get_size() == actual_mask.get_size()
    assert expected_mask.count() == actual_mask.count()
    for x in range(expected_mask.get_size()[0]):
        for y in range(expected_mask.get_size()[1]):
            assert expected_mask.get_at(x,y) == actual_mask.get_at(x,y)


def no_transfomation(p):
    """
    no_transfomation Returns its arguments un altered.
    Purpuse is to exclude the coordinate transformations by providin a callable
    object that returns the argument unchanged.
    """
    return p

###################################################################################################
class Collision_Tracker():
    def __init__(self):
        self.collisions = []

    def collision(self, collided_object):
        self.collisions.append(collided_object)

###################################################################################################
def test_polygon_drawing():
    """Test Polygon draws on surface by comparing with direct call to pygame.draw.polygon"""

    size = (100, 100)
    points = [(10, 10), (50, 50), (50, 10)]
    color = "White"

    expected_surface = pygame.surface.Surface(size)
    pygame.draw.polygon(expected_surface, color, points)

    actual_surface = pygame.surface.Surface(size)
    draw_command = Polygon(color, points, None ,CoordinateSystem.SCREEN)

    (actual_rect, actual_mask, actual_callback) = draw_command.draw(  actual_surface, no_transfomation,
    )

    assert_identical_surface(expected_surface, actual_surface)
    ###################################################################################################


def test_polygon_returnvalue():
    """Test Polygon return values after draw operation"""

    size = (100, 100)
    points = [(10, 10), (50, 50), (50, 10)]
    color = "White"
    collision_tracker = Collision_Tracker()

    expected_surface = pygame.surface.Surface(size)
    expected_rect = pygame.draw.polygon(expected_surface, color, points)
    expected_mask = None

    actual_surface = pygame.surface.Surface(size)
    draw_command = Polygon(
        color, points, collision_tracker, CoordinateSystem.SCREEN
    )

    (actual_rect, actual_mask, actual_callback) = draw_command.draw(
        actual_surface,
        no_transfomation,
    )

    assert actual_rect == expected_rect
    assert actual_callback is collision_tracker
    assert actual_mask.get_rect().width == actual_rect.width
    assert actual_mask.get_rect().height == actual_rect.height
    assert_identical_mask(expected_mask, actual_mask)


def test_text_topleft():
    """
    test_text_topleft Unittest that text is drawn at expected place
    """
    window_width = 1000
    window_height = 500

    message = "Hello World!"
    pygame.font.init()
    font = pygame.font.Font()
    antialias = True
    color = "White"
    bgcolor = None
    wraplength = 0

    screen_mapper = XYtoScreen( window_width, window_height, (10.0, 10.0), 2)

    expected_surface = pygame.surface.Surface((window_width, window_height) )
    image = font.render(message, antialias, color, bgcolor, wraplength)
    expected_surface.blit(image)

    actual_surface = pygame.surface.Surface((window_width, window_height) )
    draw_command = Text(
        NamedReferencePoint.TOPLEFT,
        CoordinateSystem.SCREEN,
        message,
        font,
        color,
        bgcolor,
        antialias,
        wraplength,
        0,
    )

    draw_command.draw(actual_surface, screen_mapper )

    expected_pixels = pygame.PixelArray(expected_surface)
    actual_pixels = pygame.PixelArray(actual_surface)
    for x in range(expected_surface.width):
        for y in range(expected_surface.height):
            assert actual_pixels[x, y] == expected_pixels[x, y]


def test_text_bottomright():
    """
    test_text_topleft Unittest that text is drawn at expected place
    """
    window_width = 1000
    window_height = 500

    message = "Hello World!"
    pygame.font.init()
    font = pygame.font.Font()
    antialias = True
    color = "White"
    bgcolor = None
    wraplength = 0

    screen_mapper = XYtoScreen(window_width, window_height, (10.0, 10.0), 2)

    expected_surface = pygame.surface.Surface((window_width, window_height))
    image = font.render(message, antialias, color, bgcolor, wraplength)
    expected_surface.blit(image,(expected_surface.width-image.width,
                          expected_surface.height-image.height) )

    actual_surface = pygame.surface.Surface((window_width, window_height))
    draw_command = Text(
        NamedReferencePoint.BOTTOMRIGHT,
        CoordinateSystem.SCREEN,
        message,
        font,
        color,
        bgcolor,
        antialias,
        wraplength,
        0,
    )

    draw_command.draw(actual_surface, screen_mapper)

    expected_pixels = pygame.PixelArray(expected_surface)
    actual_pixels = pygame.PixelArray(actual_surface)
    for x in range(expected_surface.width):
        for y in range(expected_surface.height):
            assert actual_pixels[x, y] == expected_pixels[x, y]
