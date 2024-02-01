from tkinter import Tk, Canvas, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"View\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Root(Tk):
    
    def __init__(self):
        
        super().__init__()

        # MAIN WINDOW
        self.geometry("994x480")
        self.configure(bg="#F2E8CF")
        self.title("InsectaCam")
        self.resizable(False, False)
        self.drawgui()
        

    def drawgui(self):
        
        # CANVAS
        self.C = Canvas(
            self,
            bg="#F2E8CF",
            height=480,
            width=995,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        
        # TITLE BAR INSECTACAM + PICTURE
        self.image2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.C.create_image(
            550.0,
            48.0,
            image = self.image2
        )
        self.C.create_text(
            115.0,
            11.0,
            anchor="nw",
            text="InsectaCam",
            fill="#F2E8CF",
            font=("Inter", 50 * -1)
        )
        self.image5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.C.create_image(
            61.0,
            48.0,
            image = self.image5
        )
        self.C.place(x=0,y=0)



    
