from os import getenv
from platform import system as sysname


class Save:
  spath: str  # Save file path.
  ipath: str  # Info file path.
  slot = 0

  sdata = {  # Save data.
    "newgame": 0,
    "mode": 1,  # 1=adventure, 2=fixed-party.
    "diff": 2,  # 1=normal, 2=hard.
    "started": 1,  # Enables continue option on title screen.
    "locked": 1,  # 0=locked for fixed-party, 1=unlocked for adventure.
    "cine": 1,  # Fredbear pos & next dialogue.
    "tokens": 0,
    "resetpos": 0,
    # These are the starting coords!
    "x": 1827,
    "y": 1023,
    """
    0=fazbear hills
    2=choppys woods
    5=dusting fields
    8=lilygear lake
    11=mysterious mine
    14=blacktomb yard
    17=deep-metal mine
    20=pinwheel circus
    23=glitch zone
    26=pinwheel funhouse
    50=geist lair
    """
    "area": 0,
    "seconds": 0,
    "min": 0,
    "hour": 0,

    # Characters.
    "1have": 1,   # Freddy.
    "2have": 1,   # Bonnie.
    "3have": 1,   # Chica.
    "4have": 1,   # Foxy.
    "5have": 1,   # Toy Bonnie.
    "6have": 1,   # Toy Chica.
    "7have": 1,   # Toy Freddy.
    "8have": 1,   # Mangle.
    "9have": 0,   # BB.
    "10have": 0,  # JJ.
    "11have": 0,  # Phantom Freddy.
    "12have": 0,  # Phantom Chica.
    "13have": 0,  # Phantom BB.
    "14have": 0,  # Phantom Foxy.
    "15have": 0,  # Phantom Mangle.
    "16have": 0,  # Withered Bonnie.
    "17have": 0,  # Withered Chica.
    "18have": 0,  # Withered Freddy.
    "19have": 0,  # Withered Foxy.
    "20have": 0,  # Shadow Freddy.
    "21have": 0,  # Marionette.
    "22have": 0,  # Phantom Marionette.
    "23have": 0,  # Golden Freddy.
    "24have": 0,  # Paper Pals.
    "25have": 0,  # Nighmare Freddy.
    "26have": 0,  # Nightmare Bonnie.
    "27have": 0,  # Nightmare Chica.
    "28have": 0,  # Nightmare Foxy.
    "29have": 0,  # Endo 01.
    "30have": 0,  # Endo 02.
    "31have": 0,  # Plushtrap.
    "32have": 0,  # Endoplush.
    "33have": 0,  # Springtrap.
    "34have": 0,  # RWQFSFASXC.
    "35have": 0,  # Crying Child.
    "36have": 0,  # Funtime Freddy.
    "37have": 0,  # Nightmare Fredbear.
    "38have": 0,  # Nightmare.
    "39have": 0,  # Fredbear.
    "40have": 0,  # Spring Bonnie.
    "41have": 0,  # Jack-O-Bonnie.
    "42have": 0,  # Jack-O-Chica.
    "43have": 0,  # Animdude.
    "44have": 0,  # Mr. Chipper.
    "45have": 0,  # Nightmare BB.
    "46have": 0,  # Nightmarionne.
    "47have": 0,  # Coffee.
    "48have": 0,  # Purple Guy.
  }

  # & = save slot (mode1, diff2, etc.)
  idata = {  # Info data.
    "first": 1,  # 1 if you've seen the opening cutscene.
    "mode&": 0,  # 1=adventure, 2=fixed party.
    # 1=Normal, 2=Hard (you can set this to anything as it's just a multiplier.)
    "diff&": 0,
    "hour&": 0,  # Hours played on save.
    "min&": 0,  # Minutes played on save.
    "beatgame1": 0,  # Security trophy.
    "beatgame2": 0,  # Animdude trophy.
    "beatgame3": 0,  # Chippers revenge trophy.
    "beatgame4": 0,  # 4th layer trophy.
    "beatgame5": 0,  # Clock ending trophy.
    "beatgame6": 0,  # Universe end trophy.
    "beatgame7": 0,  # Chicas magic rainbow trophy.
    "gotpearl": 0,   # Pearl trophy.
    "all": 0         # Fan trophy.
  }

  # Changes to be made.
  staged: tuple[dict[str, int], dict[str, int]] = (sdata, idata)

  def __init__(self) -> None:
    os = sysname()  # Windows | Linux | Darwin

    match os:
      case "Windows":
        base_path = "%s\\MMFApplications" %getenv("APPDATA")
        self.spath = f"{base_path}\\fnafw{self.slot}"
        self.ipath = "%s\\info" %base_path

      # Can only assume Linux would work the same way as I can't get WINE to run on my Ubuntu install :(
      case "Darwin" | "Linux":
        base_path = f"{getenv("HOME")}/.wine/drive_c/users/{getenv("USERNAME")}/AppData/Roaming/MMFApplications"
        self.spath = f"{base_path}/fnafw{self.slot}"
        self.ipath = "%s/info" %base_path

  def onefiftyseven(self, _controller) -> None:
    """
    Unlocks everything in your save, all characters,
    trophies, areas, chips, bytes, etc.
    """

    if (self.slot == 0): _controller.err("Error", "Select a slot!")
    else:
      if _controller.confirm("Confirm", "Are you sure you want to override your file to 157%?"):
        print("set slot %s to 157%% file" %self.slot)

  def write_changes(self, _controller) -> None:
    self.sdata, self.idata = self.staged

  def read(self, _controller) -> None: ...
  def prettify(self, _controller) -> None: ...
  def reset(self, _controller) -> None: ...
