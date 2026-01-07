# Author:
# Date:
# Description:

import turtle

def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle for coloring pixels. Return a turtle
        object in hidden state with its pen up. The canvas has size canv_width
        by canv_height, with a coordinate system where (0,0) is in the bottom
        left corner, and automatic re-drawing of the canvas is disabled so that
        turtle.update() must be called to update the drawing.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()

    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    screen.setworldcoordinates(0, 0, canv_width, canv_height)

    t.up() # lift the pen
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement

    return t


def midpoint(a, b):
    """ Return the midpoint between points a = (ax, ay) and b = (bx, by) """
    ax, ay = a
    bx, by = b
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    return mx, my


if __name__ == "__main__":
    import sys
    import turtle

    # width and height are given as command line arguments:
    canv_width = int(sys.argv[1])
    canv_height = int(sys.argv[2])

    # Start by calling the turtle_setup function.
    t = turtle_setup(canv_width, canv_height)

    # Then implement the pseudocode below,
    # using the above turtle to color pixels:

    # Chaos game - pseudocode from the assignment handout:
    # p = a random corner of the triangle
    # loop 10000 times:
    #     c = a random corner of the triangle
    #     m = the midpoint between p and c
    #     choose a color for m
    #     color the pixel at m
    #     p=m
