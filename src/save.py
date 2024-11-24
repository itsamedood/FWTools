from os import getenv
from platform import system as sysname


class Save:
  spath: str
  ipath: str
  slot = 0

  wdata = {
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
    "1have": 1,
    "2have": 1,
    "3have": 1,
    "4have": 1,
    "5have": 1,
    "6have": 1,
    "7have": 1,
    "8have": 1,
    "9have": 0,
    "10have": 0,
    "11have": 0,
    "12have": 0,
    "13have": 0,
    "14have": 0,
    "15have": 0,
    "16have": 0,
    "17have": 0,
    "18have": 0,
    "19have": 0,
    "20have": 0,
    "21have": 0,
    "22have": 0,
    "23have": 0,
    "24have": 0,
    "25have": 0,
    "26have": 0,
    "27have": 0,
    "28have": 0,
    "29have": 0,
    "30have": 0,
    "31have": 0,
    "32have": 0,
    "33have": 0,
    "34have": 0,
    "35have": 0,
    "36have": 0,
    "37have": 0,
    "38have": 0,
    "39have": 0,
    "40have": 0,
    "41have": 0,
    "42have": 0,
    "43have": 0,
    "44have": 0,
    "45have": 0,
    "46have": 0,
    "47have": 0,
    "48have": 0,
  }

  idata = {
    "first": 1,
    "mode&": 0,
    "diff&": 0,
    "hour&": 0,
    "min&": 0,
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

  def __init__(self) -> None:
    os = sysname()  # Windows | Linux | Darwin

    match os:
      case "Windows":
        base_path = "%s\\MMFApplications" %getenv("APPDATA")
        self.spath = f"{base_path}\\fnafw{self.slot}"
        self.ipath = "%s\\info" %base_path

      case "Linux": ...
      case "Darwin": ...
