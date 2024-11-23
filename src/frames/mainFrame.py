from tkinter import Button, Frame, Label


class MainFrame(Frame):
  def __init__(self, _parent: Frame, _controller) -> None:
    Frame.__init__(self, _parent)
    self.controller = _controller

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)

    # Create elements.
    title_label = Label(self, text="FWTools - itsamedood (C) 2024", pady=20)

    # Add elements.
    title_label.grid(row=0, column=0, columnspan=2)
