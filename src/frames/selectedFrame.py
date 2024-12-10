from tkinter import Button, Frame, Label
from util import Util


class SelectedFrame(Frame):
  """ Loaded when the user selects a slot. """

  def __init__(self, _parent: Frame, _controller) -> None:
    Frame.__init__(self, _parent)
    self.controller = _controller

    self.selected_label = Label(self, text="Slot: %i" %Util.save.slot, font=("Futura", 17))
    characters_button = Button(self, text="Characters >>>", command=lambda: self.controller.show_frame("CharacterFrame"))

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)

    # `sticky="nw"` puts this label in the top left corner.
    self.selected_label.grid(row=0, column=0, sticky="nw")
    # `sticky="ne"` puts this button in the top right corner.
    characters_button.grid(row=0, column=1, sticky="ne")

  def update_display(self):
    self.selected_label.config(text=f"Slot: {Util.save.slot}")
