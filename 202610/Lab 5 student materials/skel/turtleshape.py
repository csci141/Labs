def save_canvas(t, base_name):
    """ Save the turtle canvas that t lives on as an eps file called
        {base_name}.eps. """
    screen = t.getscreen()
    canvas = screen.getcanvas()
    canvas.postscript(file=base_name + '.eps')

#add your other functions here!

