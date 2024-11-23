from frames.mainFrame import MainFrame
from PIL import Image, ImageTk
from sys import exit
from tkinter import Frame, Tk, messagebox


class GUI(Tk):
  """ GUI for FWTools! """

  def __init__(self, *args, **kwargs) -> None:
    Tk.__init__(self, *args, **kwargs)
    self.bind("<Key>", self.on_esc)

    # Initialize main window.
    self.title("FWTools")
    self.iconbitmap("assets/logos/FWToolslogo.ico")
    self.geometry("640x480")
    self.resizable(False, False)

    # Making the window have a container where frames will go.
    # This creates the illusion of switching between menus.
    self.container = Frame(self)
    self.container.pack(side="top", fill="both", expand=True)
    self.container.grid_rowconfigure(0, weight=1)
    self.container.grid_columnconfigure(0, weight=1)

    self.frames: dict[str, Frame] = {}

    # Add each frame here.
    for F in (
      MainFrame,
    ):
      name = F.__name__
      frame = F(self.container, self)
      frame.grid(row=0, column=0, sticky="nsew")

      self.frames[name] = frame

    self.show_frame("MainFrame")

  def show_frame(self, _frame_name: str) -> None:
    try: self.frames[_frame_name].tkraise()
    except KeyError: raise Exception("%s FRAME DOESN'T EXIST." %_frame_name)

  def on_esc(self, _event):
    if _event.keysym == "Escape": exit(0)

  def err(self, _title: str, _message: str, _close=False) -> str:
    """ Creates a smaller error window to display `_message`. """

    response = messagebox.showerror(_title, _message)
    if _close: self.destroy()

    return response
