from PIL import Image, ImageTk
from tkinter import Frame, Label, Button


class MainFrame(Frame):
  """ Initial frame when launched. """

  def __init__(self, _parent: Frame, _controller) -> None:
    Frame.__init__(self, _parent)
    self.controller = _controller

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)
    self.columnconfigure(2, weight=1)

    # Create elements.
    oplogo = Image.open("assets/images/logos/FWToolslogo.png")
    rslogo = oplogo.resize(size=(210, 160))
    self.logo = ImageTk.PhotoImage(image=rslogo)


    logo_label = Label(self, image=self.logo)
    title_label = Label(self, text="Select a slot to get started.", pady=10, font=("Futura", 25))

    # Add elements.
    logo_label.grid(row=0, column=0, columnspan=3)
    title_label.grid(row=20, column=0, columnspan=3)

    # Create buttons.
    slot1_button = Button(self, text="Slot 1", command=lambda: self.controller.select_slot(1), width=15, height=2)
    slot2_button = Button(self, text="Slot 2", command=lambda: self.controller.select_slot(2), width=15, height=2)
    slot3_button = Button(self, text="Slot 3", command=lambda: self.controller.select_slot(3), width=15, height=2)

    # Add buttons.
    slot1_button.grid(row=30, column=0, padx=10, pady=10)
    slot2_button.grid(row=30, column=1, padx=10, pady=10)
    slot3_button.grid(row=30, column=2, padx=10, pady=10)
