# Author:
# Date:
# Description:

import turtle

# copied from my lab 5 solution:
def teleport(t, x, y):
    """ Move the turtle to (x, y), ensuring that nothing is drawn along the
        way. Postcondition: the turtle's orientation and up/down state is the
        same as before.
    """
    # save the current pen state
    pen_was_down = t.isdown()
    
    # pick up pen, move to coordinates
    t.up()
    t.goto(x, y)
    
    # restore pen state
    if pen_was_down:
        t.down()

# copied from lab 6, with a couple slight modifications:
def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle; return a turtle object in hidden
        state. The canvas has size canv_width by canv_height, with a
        coordinate system where (0,0) is in the center, and automatic
        re-drawing of the canvas is disabled. Set the background image to
        earth.png.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()
   
    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255
    
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement
    
    turtle.bgpic('earth.png') # set the background image
    turtle.update()
    return t

def parse_row(line):
    """ Parse a line of the csv file, returning a dict with keys
    for latitude, longitude, timestamp, and magnitude.
    Pre: line is an unprocessed string representing a line of the file.
    Post: the returned dict has the following keys with values according
          to the data in the given line of the file:
            "latitude" -> (float)
            "longitude" -> (float)
            "timestamp" -> (str)
            "magnitude" -> (float)
    """
    # split the line into its constituent numbers

    # create a dictionary and populate it with the given keys
    
    # return the resulting dictionary

def get_max_magnitude(quakes):
    """ Return the maximum magnitude of all earthquakes in quakes.
    Precondition: quakes is a nonempty list of dictionaries, each in the format
    returned by parse_row """
    

def main():
    """ Main function: plot a circle on a map for each earthquake """
    # we'll scale coordinates and canvas to be 720x360, double
    # the size of the range of lat/lon coordinates
    scale = 2.0
    
    # call turtle_setup to set up the canvas and get a turtle
    t = turtle_setup(scale * 360, scale * 180)
    
    # open earthquakes.csv for reading
    
    # parse each line of the file using parse_row and add each returned
    # dictionary into a list (skip the headers on the first line!)

    # for each earthquake dictionary in the list:
        
        # if the magnitude is larger than 2.0:
            # compute the circle radius such that the largest-magnitude
            # earthquake has radius 10, and a 0-magnitude quake would have
            # radius 0
            
            # compute the circle color such that the red value for the largest-
            # magnitude earthquake is 255, and green and blue are 255-red.
            
            # draw a circle with the calculated radius and color at
            # the scaled coordinates (longitude * scale, latitude * scale)


    # update the screen so all the circles are drawn on the canvas

if __name__ == "__main__":
    main()


