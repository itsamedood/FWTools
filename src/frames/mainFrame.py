from PIL import Image, ImageTk
from tkinter import Button, Frame, Label


class MainFrame(Frame):
  def __init__(self, _parent: Frame, _controller) -> None:
    Frame.__init__(self, _parent)
    self.controller = _controller

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)

    # Create elements.
    oplogo = Image.open("assets/logos/FWToolslogo.png")
    oplogo = oplogo.resize((200, 150))
    logo = ImageTk.PhotoImage(oplogo)


    logo_label = Label(self, image=logo)
    # title_label = Label(self, text="FWTools - itsamedood (C) 2024", pady=10, font=("Arial", 25))

    # Add elements.
    logo_label.grid(row=0, column=0, columnspan=2)
    # title_label.grid(row=20, column=0, columnspan=2)
