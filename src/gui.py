from frames.mainFrame import MainFrame
from PIL import Image, ImageTk
from sys import exit
from tkinter import Frame, Menu, Tk, messagebox


class GUI(Tk):
  """ GUI for FWTools! """

  def __init__(self, *args, **kwargs) -> None:
    Tk.__init__(self, *args, **kwargs)
    self.bind("<Key>", self.on_esc)
    self.selected_slot = 0  # 0 means none are selected.

    # Initialize main window.
    # The app will be `Python` but PyInstaller will rename the exec. to `FWTools`.
    self.title("FWTools")
    self.geometry("640x480")
    self.configure(bg="gray")
    self.attributes("-alpha", 0.8)  # Make window a bit transparent.
    self.resizable(False, False)

    icon = ImageTk.PhotoImage(Image.open("assets/logos/FWToolslogo.png"))
    self.iconphoto(True, icon)

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

  def format_save(self):
    """
    Makes your save easier to read.
    """

    ...

  def reset_save(self): ...
  def select_slot_one(self): self.selected_slot = 1
  def select_slot_two(self): self.selected_slot = 2
  def select_slot_tre(self): self.selected_slot = 3


if __name__ == "__main__":
  # Create GUI instance and set custom menu for it.
  menu = Menu(gui:=GUI())
  gui.config(menu=menu)

  # Create menus.
  # Gotta do it here to avoid errors :(
  slot_menu = Menu(gui)
  extra_menu = Menu(gui)
  debug_menu = Menu(gui)

  # Add menu button cascades.
  menu.add_cascade(label="File", menu=slot_menu)
  menu.add_cascade(label="Extra", menu=extra_menu)
  menu.add_cascade(label="Debug", menu=debug_menu)

  # Add things to cascades.
  # File cascade.
  slot_menu.add_radiobutton(label="Slot 1", command=gui.select_slot_one)
  slot_menu.add_radiobutton(label="Slot 2", command=gui.select_slot_two)
  slot_menu.add_radiobutton(label="Slot 3", command=gui.select_slot_tre)
  slot_menu.add_separator()
  slot_menu.add_command(label="Format", command=gui.format_save)
  slot_menu.add_command(label="Reset", command=gui.reset_save)
  slot_menu.add_separator()
  slot_menu.add_command(label="Exit", command=gui.quit)

  # Extra cascade.
  extra_menu.add_command(label="Replay First Cutscene", command=lambda: print("set first=0 in info"))

  # Debug cascade.
  debug_menu.add_command(label="Show Selected Slot", command=lambda: gui.err("Selected Slot:", f"{gui.selected_slot}"))

  gui.mainloop()
