from os import scandir
from platform import system
from PIL import Image, ImageTk, ImageEnhance
from random import randint
from tkinter import Canvas, Event, Frame, Label, Scrollbar
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

      portrait_label.bind("<Button-1>", lambda _e, _i=len(self.portrait_imgs): self.on_portrait_click(_i))

      self.portrait_imgs.append((og_img, portrait_img, portrait_label, False))

    # Organizes the portraits, 5 per column.
    for og_img, img, lbl, locked in self.portrait_imgs:
      lbl.grid(row=row, column=column)
      if column % 5 == 0:
        row += 1
        column = 1
      else: column += 1

    self.determine_portraits()

    # Make locked characters more transparent, and unlocked, leave alone.
    # for i, (og_img, img, lbl, locked) in enumerate(self.portrait_imgs):
    #   if Util.save.sdata[f"{i+1}have"] == 0:  # Change this condition!
    #     enhancer = ImageEnhance.Brightness(og_img)
    #     locked = enhancer.enhance(self.LOCKED_ALPHA)
    #     locked_img = ImageTk.PhotoImage(locked)

    #     lbl.configure(image=locked_img)
    #     self.portrait_imgs[i] = (og_img, locked_img, lbl, True)

    scrollable_frame.bind("<Configure>", self.update_scrollregion)
    self.canvas.bind_all("<MouseWheel>", self.on_scroll)

  def determine_portraits(self) -> None:
    """ Make locked characters more transparent, and unlocked, leave alone. """

    for i, (og_img, img, lbl, locked) in enumerate(self.portrait_imgs):
      locked = Util.save.sdata[f"{i+1}have"] == 0
      limg = ImageTk.PhotoImage(og_img if not locked else ImageEnhance.Brightness(og_img).enhance(self.LOCKED_ALPHA))

      lbl.configure(image=limg)
      self.portrait_imgs[i] = (og_img, limg, lbl, locked)

  def on_portrait_click(self, _portrait: int):
    """ Triggers when a portrait is clicked on. Toggles "locked" (transparent) or "unlocked". """
    og_img, img, lbl, locked = self.portrait_imgs[_portrait]
    locked = not locked

    limg = ImageTk.PhotoImage(og_img if not locked else ImageEnhance.Brightness(og_img).enhance(self.LOCKED_ALPHA))
    lbl.configure(image=limg)

    self.portrait_imgs[_portrait] = (og_img, limg, lbl, locked)
    Util.save.staged[0][f"{_portrait}have"] = 0 if locked else 1

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
