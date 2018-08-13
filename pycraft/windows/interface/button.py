import glooey
from .label import Label


class Button(glooey.Button):
    Label = Label
    custom_alignment = 'fill'

    # More often you'd specify images for the different rollover states, but
    # we're just using colors here so you won't have to download any files
    # if you want to run this code.

    class Base(glooey.Background):
        custom_color = '#204a87'

    class Over(glooey.Background):
        custom_color = '#3465a4'

    class Down(glooey.Background):
        custom_color = '#729fcff'

    # Beyond just setting class variables in our widget subclasses, we can
    # also implement new functionality.  Here we just print a programmed
    # response when the button is clicked.

    def __init__(self, text, response):
        super(Button, self).__init__(text)
        self.response = response
