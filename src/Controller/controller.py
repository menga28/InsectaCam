from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from View.gui import Gui
from Controller.singleInsectController import singleInsectController


class Controller:

    def __init__(self, view: Gui) :
        self.view = view
        self.singleInsectController = singleInsectController(view)

    def start(self):
        #self.view.switch("singleinsectgui")
        self.view.start_mainloop()



