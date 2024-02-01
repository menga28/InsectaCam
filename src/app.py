from View.gui import Gui
from Controller.controller import Controller

def main():
    view = Gui()
    controller = Controller(view)
    controller.start()

if __name__ == "__main__":
    main()


