from drawing_tools import XYtoScreen

def test_mapping_bottomleft():
    test_window_width = 1000
    test_window_height = 500
    bottomleft = ( 0, 0 )
    scaling_factor = 2
    transformer = XYtoScreen(
        test_window_width,
        test_window_height,
        bottomleft,
        scaling_factor)

    assert (0, test_window_height) == transformer(bottomleft)


def test_mapping_topleft():
    test_window_width = 1000
    test_window_height = 500
    bottomleft = (0, 0)
    pixels_per_unit = 2
    transformer = XYtoScreen(
        test_window_width, test_window_height, bottomleft, pixels_per_unit
    )

    assert (0, 0) == transformer( (0, test_window_height/pixels_per_unit))


def test_mapping_mid():
    test_window_width = 1000
    test_window_height = 500
    bottomleft = (0, 0)
    pixels_per_unit = 2
    transformer = XYtoScreen(
        test_window_width, test_window_height, bottomleft, pixels_per_unit
    )

    assert (500, 250) == transformer( ( test_window_width / 2 / pixels_per_unit, test_window_height / 2 / pixels_per_unit ) )


def test_mapping_topright():
    test_window_width = 1000
    test_window_height = 500
    bottomleft = (0, 0)
    pixels_per_unit = 2
    transformer = XYtoScreen(
        test_window_width, test_window_height, bottomleft, pixels_per_unit
    )

    assert (test_window_width, 0) == transformer(
        (
            test_window_width / pixels_per_unit,
            test_window_height / pixels_per_unit,
        )
    )


def test_mapping_offset_topleft():
    test_window_width = 1000
    test_window_height = 500
    bottomleft = (100, 100)
    pixels_per_unit = 2
    transformer = XYtoScreen(
        test_window_width, test_window_height, bottomleft, pixels_per_unit
    )

    assert (0,0) == transformer( ( 100,100+test_window_height / pixels_per_unit) )
