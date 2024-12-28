from os import scandir
from platform import system
from PIL import Image, ImageTk, ImageEnhance
from random import randint
from tkinter import Canvas, Event, Frame, Label, Scrollbar, Toplevel, Entry, Button
from util import Util


class CharacterFrame(Frame):
  """ Select characters to mark as locked (transparent) or unlocked. """

  LOCKED_ALPHA = 0.4

  def __init__(self, _parent: Frame, _controller) -> None:
    Frame.__init__(self, _parent)
    self.controller = _controller

    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.canvas = Canvas(self, width=self.controller.winfo_width(), height=self.controller.winfo_height())
    self.canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    scrollable_frame = Frame(self.canvas, width=self.controller.winfo_width(), height=self.controller.winfo_height())

    self.canvas.configure(yscrollcommand=scrollbar.set)
    self.canvas.create_window(0, 0, window=scrollable_frame, anchor="nw")

    # PIL Image, PhotoImage for display, Label that displays the image, and "locked" state.
    self.portrait_imgs: list[tuple[Image.ImageFile.ImageFile, ImageTk.PhotoImage, Label, bool]] = []
    base_path = "assets/images/portraits"
    portraits = [f"{base_path}/{p.name}" for p in scandir(base_path)]
    row, column = 2, 1
    portraits.sort()  # Well that was easy!

    # Add character portraits (5 per row).
    for portrait in portraits:
      og_img = Image.open(portrait)
      portrait_img = ImageTk.PhotoImage(og_img)
      portrait_label = Label(scrollable_frame, image=portrait_img)

      # Left click.
      portrait_label.bind("<Button-1>", lambda _e, _i=len(self.portrait_imgs): self.on_portrait_left_click(_i))

      # Button-2 is scrollwheel-click, and Button-3 is right-click,
      # but on MacOS Button-2 worked as right-click (trackpad?), so I'll just bind both.
      portrait_label.bind("<Button-2>", lambda _e, _i=len(self.portrait_imgs): self.on_portrait_right_click(_i))
      portrait_label.bind("<Button-3>", lambda _e, _i=len(self.portrait_imgs): self.on_portrait_right_click(_i))

      self.portrait_imgs.append((og_img, portrait_img, portrait_label, False))

    # Organizes the portraits, 5 per column.
    for og_img, img, lbl, locked in self.portrait_imgs:
      lbl.grid(row=row, column=column)
      if column % 5 == 0:
        row += 1
        column = 1
      else: column += 1

    self.determine_portraits()

    scrollable_frame.bind("<Configure>", self.update_scrollregion)
    self.canvas.bind_all("<MouseWheel>", self.on_scroll)

    # Instructions.
    left_click_label = Label(scrollable_frame, text="Left-click to toggle locked/unlocked.", font=("Futura", 12))
    right_click_label = Label(scrollable_frame, text="Right-click to set level and XP.", font=("Futura", 12))

    left_click_label.grid(row=2, column=6, columnspan=5)
    right_click_label.grid(row=3, column=6, columnspan=5)

    # Save changes button.
    save_button = Button(scrollable_frame, text="Save Changes", command=self.on_save, font=("Futura", 18))

    save_button.grid(row=4, column=6, columnspan=5, pady=10)

  def on_save(self) -> None:
    """ Save changes to the save file. """

    # Will actually write the changes to the save file, too lazy for now.
    self.controller.success("Changes saved!", True)

  def determine_portraits(self) -> None:
    """ Make locked characters more transparent, and unlocked, leave alone. """

    for i, (og_img, img, lbl, locked) in enumerate(self.portrait_imgs):
      locked = Util.save.sdata[f"{i+1}have"] == 0
      limg = ImageTk.PhotoImage(og_img if not locked else ImageEnhance.Brightness(og_img).enhance(self.LOCKED_ALPHA))

      lbl.configure(image=limg)
      self.portrait_imgs[i] = (og_img, limg, lbl, locked)

  def on_portrait_left_click(self, _portrait: int):
    """ Triggers when a portrait is clicked on. Toggles "locked" (transparent) or "unlocked". """
    og_img, img, lbl, locked = self.portrait_imgs[_portrait]
    locked = not locked

    limg = ImageTk.PhotoImage(og_img if not locked else ImageEnhance.Brightness(og_img).enhance(self.LOCKED_ALPHA))
    lbl.configure(image=limg)

    self.portrait_imgs[_portrait] = (og_img, limg, lbl, locked)
    Util.save.staged[0][f"{_portrait}have"] = 0 if locked else 1

  def on_portrait_right_click(self, _portrait: int):
    """
    Triggers when a portrait is right-clicked on (and that character is unlocked).
    Will bring up a smaller menu for setting character levels and XP to next level.
    """

    # Petty moment.
    if Util.save.sdata[f"{_portrait+1}have"] == 0:
      self.controller.err("Character is locked!")
      return

    # Create a new top-level window.
    def on_esc(_e):  # So you can use Escape to close the top-level window.
      if _e.keysym == "Escape": top.destroy()

    top = Toplevel(self)
    top.title(f"Set Level and XP (character {_portrait+1})")
    top.geometry("365x150")
    top.resizable(False, False)
    top.attributes("-alpha", 0.95)
    top.bind("<Key>", on_esc)

    # Level entry.
    Label(top, text="Level:", font=("Futura", 12)).grid(row=0, column=0, padx=5, pady=5)
    level_entry = Entry(top)
    level_entry.grid(row=0, column=1, padx=5, pady=5)

    # XP entry.
    Label(top, text="XP to next level (0=100):", font=("Futura", 12)).grid(row=1, column=0, padx=5, pady=5)
    xp_entry = Entry(top)
    xp_entry.grid(row=1, column=1, padx=5, pady=5)

    def save_changes():
      try:
        level = int(level_entry.get())
        xp = int(xp_entry.get())
        Util.save.staged[0][f"{_portrait}lv"] = level
        Util.save.staged[0][f"{_portrait}next"] = xp
        top.destroy()

        self.controller.success("Changes saved!")
      except ValueError: self.controller.err("Level and XP must be integers!")

    # Save button
    Button(top, text="Save", command=save_changes).grid(row=2, column=0, columnspan=2, pady=10)

  def update_scrollregion(self, _e):
    self.canvas.configure(scrollregion=self.canvas.bbox("all"))

  def on_scroll(self, _e: Event):
    # Windows & MacOS scroll.
    if _e.delta:
      if system() == "Darwin":
        # Best I could do to make the scrolling not awful on MacOS.
        # Calculate a fraction to scroll.
        scroll_fraction = _e.delta / 300  # Adjust divisor for finer scrolling (larger = slower).
        current_view = self.canvas.yview()
        new_view_start = max(0, min(1, current_view[0] - scroll_fraction))  # Clamp between 0 and 1.
        self.canvas.yview_moveto(new_view_start)

      # Supposedly the issue isn't present on Windows, but I'll test that.
      else: self.canvas.yview_scroll(-1 if _e.delta > 0 else 1, "units")

    # 4 = scrollwheel up. | 5 = scrollwheel down.
    elif _e.num == 4: self.canvas.yview_scroll(-1, "units")
    elif _e.num == 5: self.canvas.yview_scroll(1, "units")
