import glooey


class Layout:
    def __init__(self, type):
        if type == 'VBox':
            layout = glooey.VBox()
        else:
            layout = glooey.Grid()
        self.layout = layout

    def get_layout(self):
        return self.layout
