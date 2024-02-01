from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"View\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class singleInsectGUI(Canvas):
    
    def __init__(self, master):
    
        #Frame.__init__(self,master,bg="red",height=383,width=994)
        Canvas.__init__(self, master,bg="#F2E8CF",height=480, width=994,bd=0,highlightthickness=0,relief="ridge")
        self.master = master
        self.place(x=0,y=0)
        #self.pack_propagate(False)
        self.drawgui()

            
    def drawgui(self):
        # MAIN WINDOW
        # self.C = Canvas(
        #     self,
        #     bg="#F2E8CF",
        #     height=480,
        #     width=994,
        #     bd=0,
        #     highlightthickness=0,
        #     relief="ridge"
        # )
        # #self.C.pack()
        # self.C.place(x=0, y=0)
        
        # TITLE BAR INSECTACAM + PICTURE
        self.image2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.create_image(
            550.0,
            48.0,
            image = self.image2
        )
        self.create_text(
            115.0,
            11.0,
            anchor="nw",
            text="InsectaCam",
            fill="#F2E8CF",
            font=("Inter", 50 * -1)
        )
        self.image5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.create_image(
            61.0,
            48.0,
            image = self.image5
        )

        # INSECT SPECIES
        self.image1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.create_image(
            339.0,
            206.0,
            image = self.image1
        )
        self.create_text(
            284.0,
            197.0,
            anchor="nw",
            text="Insect species\n",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        # SPECIES DETECTED
        self.image3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.create_image(
            611.0,
            206.0,
            image = self.image3
        )
        self.speciesDetected = self.create_text(
            497.0,
            197.0,
            anchor="nw",
            text="Species detected",
            fill="#F2E8CF",
            font=("Inter", 16 * -1)
        )

        # SELECTED IMAGE
        self.image9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.create_image(
            115.0,
            147.0,
            image = self.image9
        )
        self.create_text(
            29.0,
            138.0,
            anchor="nw",
            text="Selected image",
            fill="#F2E8CF",
            font=("Inter", 16 * -1)
        )
        self.image7 = PhotoImage(file=relative_to_assets("image_7.png"))
        self.upload_frame = self.create_image(
            113.554443359375,
            281.0,
            image = self.image7
        )
        
        # UPLOAD BUTTON
        self.image4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.create_image(
            115.0,
            415.0,
            image = self.image4
        )
        self.upload_button = Button(
            self,
            image = self.image4,
            borderwidth=0
        )
        #self.upload_button.pack()
        self.upload_button.place(x=74, y=390)

        # INSECTS SPECIES DETECTED
        self.image10 = PhotoImage(file=relative_to_assets("image_10.png"))
        self.create_image(
            339.0,
            276.0,
            image = self.image10
        )
        self.create_text(
            256.0,
            265.0,
            anchor="nw",
            text="Insect species detected",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        # RESULTS
        self.image11 = PhotoImage(file=relative_to_assets("image_11.png"))
        self.create_image(
            611.0,
            324.0,
            image = self.image11
        )
        self.create_text(
            559.0,
            273.0,
            anchor="nw",
            text="Lucilia Sericata\n\n",
            fill="#F2E8CF",
            font=("Inter", 16 * -1)
        )
        self.create_text(
            558.0,
            343.0,
            anchor="nw",
            text="Piophila Casei\n",
            fill="#F2E8CF",
            font=("Inter", 16 * -1)
        )
        self.create_text(
            559.0,
            308.0,
            anchor="nw",
            text="Musca Domestica\n",
            fill="#F2E8CF",
            font=("Inter", 16 * -1)
        )
        self.lsPercentage = self.create_text(
            493.0,
            273.0,
            anchor="nw",
            text="0%",
            fill="#F2E8CF",
            font=("Inter", 16 * -1, "bold")
        )
        self.mdPercentage = self.create_text(
            493.0,
            309.0,
            anchor="nw",
            text="0%",
            fill="#F2E8CF",
            font=("Inter", 16 * -1, "bold")
        )
        self.pcPercentage = self.create_text(
            492.0,
            345.0,
            anchor="nw",
            text="0%",
            fill="#F2E8CF",
            font=("Inter", 16 * -1, "bold")
        )
        #self.C.pack()
        self.place(x=0, y=0)






