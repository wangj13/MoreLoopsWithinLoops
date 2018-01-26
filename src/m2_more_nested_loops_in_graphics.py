"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jixi Wang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """

    rectangle.attach_to(window)
    x1 = rectangle.corner_1.x
    x2 = rectangle.corner_2.x
    y1 = rectangle.corner_1.y
    y2 = rectangle.corner_2.y
    for j in range(n):
        x1 = x1 - rectangle.get_width() / 2
        x2 = x2 - rectangle.get_width() / 2
        y1 = y1 - rectangle.get_height()
        y2 = y2 - rectangle.get_height()
        rectangle = rg.Rectangle(rg.Point(x1, y1), rg.Point(x2, y2))
        rectangle.attach_to(window)

        newx1 = x1 - rectangle.get_width()
        newx2 = x2 - rectangle.get_width()
        new_rectangle = rg.Rectangle(rg.Point(newx1, y1), rg.Point(newx2, y2))
        new_rectangle.attach_to(window)

        for k in range(n-j):
            newx1 = newx1 - rectangle.get_width()
            newx2 = newx2 - rectangle.get_width()
            new_rectangle2 = rg.Rectangle(rg.Point(newx1, y1), rg.Point(newx2,
                                                                        y2))
            new_rectangle2.attach_to(window)

    window.render()

    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
