from PIL import Image, ImageTk
from tkinter import Button, Frame, Label


class MainFrame(Frame):
  """ Initial frame when launched. """

  def __init__(self, _parent: Frame, _controller) -> None:
    Frame.__init__(self, _parent)
    self.controller = _controller

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)

    # Create elements.
    oplogo = Image.open("assets/logos/FWToolslogo.png")
    rslogo = oplogo.resize(size=(210, 160))
    self.logo = ImageTk.PhotoImage(image=rslogo)


    logo_label = Label(self, image=self.logo)
    title_label = Label(self, text="FWTools - © 2024, itsamedood", pady=10, font=("Futura", 25))

    # Add elements.
    logo_label.grid(row=0, column=0, columnspan=2)
    title_label.grid(row=20, column=0, columnspan=2)