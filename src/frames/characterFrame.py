from platform import system
from tkinter import Canvas, Event, Frame, Label, Scrollbar
from util import Util


class CharacterFrame(Frame):
  def __init__(self, _parent: Frame, _controller) -> None:
    Frame.__init__(self, _parent)
    self.controller = _controller

    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.canvas = Canvas(self, bg="red", width=self.controller.winfo_width(), height=self.controller.winfo_height())
    self.canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    scrollable_frame = Frame(self.canvas, width=self.controller.winfo_width(), height=self.controller.winfo_height())

    self.canvas.configure(yscrollcommand=scrollbar.set)
    self.canvas.create_window(0, 0, window=scrollable_frame, anchor="nw")

    for i in range(30):
      label = Label(scrollable_frame, text=f"Label {i}", font=("Futura", 25))
      label.grid(row=i, column=0, pady=2, padx=5)

    scrollable_frame.bind("<Configure>", self.update_scrollregion)
    self.canvas.bind_all("<MouseWheel>", self.on_scroll)

  def update_scrollregion(self, _e):
    self.canvas.configure(scrollregion=self.canvas.bbox("all"))

  def on_scroll(self, _e: Event):
    # Windows & MacOS scroll.
    if _e.delta:
      self.canvas.yview_scroll(-1 if _e.delta > 0 else 1, "units")

    # Scroll up.
    elif _e.num == 4: self.canvas.yview_scroll(-1, "units")
    # Scroll down.
    elif _e.num == 5: self.canvas.yview_scroll(1, "units")
