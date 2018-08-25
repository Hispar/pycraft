from pycraft.windows.interface.title import Title
from pycraft.windows.layouts.layout import Layout


class RunningLayout(Layout):
    def __init__(self):
        super(RunningLayout, self).__init__('Grid')
        title = Title("")
        title.set_alignment('top left')

        self.title = title
        self.layout.add(0, 0, title)

    def set_title(self, title):
        self.title.set_text(title)
