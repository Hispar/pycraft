from pycraft.windows.interface.button import Button
from pycraft.windows.interface.title import Title
from pycraft.windows.layouts.layout import Layout


class MainScreenLayout(Layout):
    def __init__(self):
        super(MainScreenLayout, self).__init__('VBox')
        self.layout.alignment = 'center'

        self.title = Title("Pycraft")
        self.layout.add(self.title)

        self.start = Button("Start Game")
        # start.push_handlers(on_click=lambda w: self.start())
        self.layout.add(self.start)

        self.resume = Button("Resume Game")
        # resume.push_handlers(on_click=lambda w: self.resume())
        self.layout.add(self.resume)

    def get_start_btn(self):
        return self.start

    def get_resume_btn(self):
        return self.resume
