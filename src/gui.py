from frames.characterFrame import CharacterFrame
from frames.mainFrame import MainFrame
from frames.selectedFrame import SelectedFrame
from PIL import Image, ImageTk
from tkinter import Frame, Menu, Tk, messagebox
from util import Util


class GUI(Tk):
  """ GUI for FWTools! """

  frame_stack: list[str] = []

  def __init__(self, *args, **kwargs) -> None:
    Tk.__init__(self, *args, **kwargs)
    self.bind("<Key>", self.on_esc)

    # Initialize main window.
    # The app will be `Python` but PyInstaller will rename the exec. to `FWTools`.
    self.title("FWTools")
    self.geometry("640x480")
    self.attributes("-alpha", 0.8)  # Make window a bit transparent.
    self.resizable(False, False)

    icon = ImageTk.PhotoImage(Image.open("assets/images/logos/FWToolslogo.png"))
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
      SelectedFrame,
      CharacterFrame
    ):
      name = F.__name__
      frame = F(self.container, self)
      frame.grid(row=0, column=0, sticky="nsew")

      self.frames[name] = frame

    self.show_frame("MainFrame")

  def show_frame(self, _frame_name: str) -> None:
    try:
      self.frame_stack.append(_frame_name)
      self.frames[_frame_name].tkraise()

    except KeyError: raise Exception("%s FRAME DOESN'T EXIST." %_frame_name)

  def on_esc(self, _event) -> None:
    """ Triggered when [Escape] is pressed. """

    if _event.keysym == "Escape":
      if len(self.frame_stack) < 2 or self.frame_stack[-1] == "SelectedFrame": self.quit()
      else:
        # I'm ashamed to admit this took like 20 minutes...
        self.frame_stack.pop()
        self.show_frame(self.frame_stack[-1])
        self.frame_stack.pop()

  def err(self, _title: str, _message: str, _close=False) -> str:
    """ Creates a smaller error window to display `_message`. """

    response = messagebox.showerror(_title, _message)
    if _close: self.destroy()

    return response

  def confirm(self, _title: str, _message: str) -> bool:
    """ Creates a 'are you sure?' window. """

    return messagebox.askokcancel(_title, _message)

  def format_save(self) -> None:
    """
    Makes your save easier to read.
    """

    ...

  def reset_save(self) -> None:
    """
    Resets your save back to what you would
    see if you just started a new save file.
    """

    ...

  def onefiftyseven(self) -> None:
    if (Util.save.slot == 0): self.err("Error", "Select a slot!")
    else:
      if self.confirm("Confirm", "Are you sure you want to override your file to 157%?"):
        print("set slot %s to 157%% file" %Util.save.slot)

  def select_slot(self, _slot: int) -> None:
    Util.save.slot = _slot
    Util.save.spath = f"{Util.save.spath[:-1]}{_slot}"
    selected_frame = self.frames["SelectedFrame"]
    selected_frame.update_display()
    self.show_frame("SelectedFrame")

  # def select_slot_one(self):
  #   self.selected_slot = 1

  # def select_slot_two(self): self.selected_slot = 2

  # def select_slot_tre(self): self.selected_slot = 3


def setup_menu(_gui: GUI) -> Menu:
  menu = Menu(_gui)

  # Create menus.
  slot_menu = Menu(gui)
  extra_menu = Menu(gui)
  debug_menu = Menu(gui)

  # Add menu button cascades.
  menu.add_cascade(label="File", menu=slot_menu)
  menu.add_cascade(label="Extra", menu=extra_menu)
  menu.add_cascade(label="Debug", menu=debug_menu)

  # Add things to cascades.
  # File cascade.
  slot_menu.add_radiobutton(label="Slot 1", command=lambda: gui.select_slot(1))
  slot_menu.add_radiobutton(label="Slot 2", command=lambda: gui.select_slot(2))
  slot_menu.add_radiobutton(label="Slot 3", command=lambda: gui.select_slot(3))
  slot_menu.add_separator()
  slot_menu.add_command(label="Format", command=gui.format_save)
  slot_menu.add_command(label="Reset", command=gui.reset_save)
  slot_menu.add_command(label="157%", command=gui.onefiftyseven)
  slot_menu.add_separator()
  slot_menu.add_command(label="Exit", command=gui.quit)

  # Extra cascade.
  extra_menu.add_command(label="Replay First Cutscene", command=lambda: print("set first=0 in info"))

  # Debug cascade.
  debug_menu.add_command(label="Show Selected Slot", command=lambda: gui.err("Selected Slot:", f"{Util.save.spath}"))

  return menu


if __name__ == "__main__":
  # Create GUI instance and set custom menu for it.
  menu = setup_menu(gui:=GUI())
  gui.config(menu=menu)

  gui.mainloop()  # Run.
