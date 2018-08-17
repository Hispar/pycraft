from pycraft.windows.interface.title import Title
from pycraft.windows.layouts.layout import Layout


class LoadingLayout(Layout):
    def __init__(self):
        super(LoadingLayout, self).__init__('VBox')
        self.layout.alignment = 'center'

        self.title = Title("Cargando")
        self.layout.add(self.title)
