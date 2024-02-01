from typing import TypedDict
from .root import Root
from .singleInsectGUI import singleInsectGUI

class Guis(TypedDict):
    singleinsectgui: singleInsectGUI

class Gui:

    def __init__(self):
        self.root = Root()
        self.guis: Guis = {}  # type: ignore
        self.current_gui = None
        self.add_gui(singleInsectGUI, "singleinsectgui")
        self.switch("singleinsectgui")

    
    def add_gui(self, Gui, name: str) -> None:
        self.guis[name] = Gui(self.root)
        #self.guis[name].place(x=0,y=0)

    # def switch(self, name: str) -> None:
    #     frame = self.frames[name]
    #     #frame.tkraise()


    # def _add_canvas(self, Canvas, name):
    #         self.canvas[name] = Canvas(self.root)
    #         self.canvas[name].place(x=0, y=0, anchor="center")

    def switch(self, name: str) -> None:
            self.new_gui = self.guis[name]
            if self.current_gui is not None:
                self.current_gui.destroy()
            self.current_gui = self.new_gui
            self.current_gui.place(x=0, y=0)
            #self.current_gui.tkRaise()

    def start_mainloop(self):
            self.root.mainloop()


