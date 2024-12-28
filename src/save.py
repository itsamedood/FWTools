from os import getenv
from os.path import exists
from platform import system as sysname
from re import match


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
    "resetpos": 0,  # 0=fazbear hills, 1=wherever you last were (boss fights).

    # These are the starting coords!
    "x": 1827,
    "y": 1023,

    # 0=fazbear hills
    # 2=choppys woods
    # 5=dusting fields
    # 8=lilygear lake
    # 11=mysterious mine
    # 14=blacktomb yard
    # 17=deep-metal mine
    # 20=pinwheel circus
    # 23=glitch zone
    # 26=pinwheel funhouse
    # 50=geist lair
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

    # Character levels.
    "1lv": 1,
    "2lv": 1,
    "3lv": 1,
    "4lv": 1,
    "5lv": 1,
    "6lv": 1,
    "7lv": 1,
    "8lv": 1,
    "9lv": 0,
    "10lv": 0,
    "11lv": 0,
    "12lv": 0,
    "13lv": 0,
    "14lv": 0,
    "15lv": 0,
    "16lv": 0,
    "17lv": 0,
    "18lv": 0,
    "19lv": 0,
    "20lv": 0,
    "21lv": 0,
    "22lv": 0,
    "23lv": 0,
    "24lv": 0,
    "25lv": 0,
    "26lv": 0,
    "27lv": 0,
    "28lv": 0,
    "29lv": 0,
    "30lv": 0,
    "31lv": 0,
    "32lv": 0,
    "33lv": 0,
    "34lv": 0,
    "35lv": 0,
    "36lv": 0,
    "37lv": 0,
    "38lv": 0,
    "39lv": 0,
    "40lv": 0,
    "41lv": 0,
    "42lv": 0,
    "43lv": 0,
    "44lv": 0,
    "45lv": 0,
    "46lv": 0,
    "47lv": 0,
    "48lv": 0,

    # Character XP to next level.
    "1next": 100,
    "2next": 100,
    "3next": 100,
    "4next": 100,
    "5next": 100,
    "6next": 100,
    "7next": 100,
    "8next": 100,
    "9next": 0,
    "10next": 0,
    "11next": 0,
    "12next": 0,
    "13next": 0,
    "14next": 0,
    "15next": 0,
    "16next": 0,
    "17next": 0,
    "18next": 0,
    "19next": 0,
    "20next": 0,
    "21next": 0,
    "22next": 0,
    "23next": 0,
    "24next": 0,
    "25next": 0,
    "26next": 0,
    "27next": 0,
    "28next": 0,
    "29next": 0,
    "30next": 0,
    "31next": 0,
    "32next": 0,
    "33next": 0,
    "34next": 0,
    "35next": 0,
    "36next": 0,
    "37next": 0,
    "38next": 0,
    "39next": 0,
    "40next": 0,
    "41next": 0,
    "42next": 0,
    "43next": 0,
    "44next": 0,
    "45next": 0,
    "46next": 0,
    "47next": 0,
    "48next": 0,

    # Party slots.
    "s1": 1,
    "s2": 2,
    "s3": 3,
    "s4": 4,
    "s5": 5,
    "s6": 6,
    "s7": 7,
    "s8": 8,

    # Chip slots.
    "active1": 0,
    "active2": 0,
    "active3": 0,
    "active4": 0,

    # Byte slots.
    "active1b": 0,
    "active2b": 0,
    "active3b": 0,
    "active4b": 0,

    # Clocks done.
    "find": 0,  # Current clock.
    "g1": 0,
    "g2": 0,
    "g3": 0,
    "g4": 0,
    "g5": 0,
    "g6": 0,

    # Unlocked chips.
    "c1": 0,
    "c2": 0,
    "c3": 0,
    "c4": 0,
    "c5": 0,
    "c6": 0,
    "c7": 0,
    "c8": 0,
    "c9": 0,
    "c10": 0,
    "c11": 0,
    "c12": 0,
    "c13": 0,
    "c14": 0,
    "c15": 0,
    "c16": 0,
    "c17": 0,
    "c18": 0,
    "c19": 0,
    "c20": 0,
    "c21": 0,

    # Purchased bytes.
    "p1": 0,
    "p2": 0,
    "p3": 0,
    "p4": 0,
    "p5": 0,
    "p6": 0,
    "p7": 0,
    "p8": 0,
    "p9": 0,
    "p10": 0,
    "p11": 0,
    "p12": 0,
    "p13": 0,
    "p14": 0,
    "p15": 0,
    "p16": 0,
    "p17": 0,
    "p18": 0,
    "p19": 0,
    "p20": 0,
    "p21": 0,

    "sw1": 0,  # Choppy's Woods.
    "sw2": 0,  # Lilygear Lake.
    "sw3": 0,  # Blacktomb Yard.
    "sw4": 0,  # Pinwheel Circus.
    "sw5": 0,  # Key room.
    "sw6": 0,  # Dusting Fields gate.
    "sw7": 0,  # Fazbear Hills gate.
    "sw8": 0,  # Lilygear Lake gate.
    "sw9": 0,  # Blacktomb Yard gate.

    "w3": 0,  # Entered Dusting Fields.
    "key": 0,  # Have key.
    "portal": 0,  # No idea, but probably: 0=no scott portal, 1=scott portal.

    "armor": 0,  # 0=default, 1=reinforced, 2=steel, 10=titanium.
    "ar1": 0,  # Reinforced armor purchased.
    "ar2": 0,  # Steel armor purchased.
    "ar3": 0,  # Titanium armor purchased.
    "fish": 0,  # Idk how this one behaves lol.
    "pearl": 0,  # Number of times pearl has been caught.
    "last": 0,  # Encountered Scott.
    "beatgame1": 0,  # Beat Security.
    "beatgame2": 0,  # Beat Scott.
    "beatgame3": 0,  # Beat Chipper's Revenge.
    "beatgame7": 0,  # Beat Chica's Magic Rainbow.
    "showend": 0,  # Show end cutscene.
  }

  idata = {  # Info data.
    "first": 0,  # 1 if you've seen the opening cutscene.
    "mode1": 0,  # 1=adventure, 2=fixed party.
    # 1=Normal, 2=Hard (you can set this to anything as it's just a multiplier.)
    "mode2": 0,
    "mode3": 0,
    "diff1": 0,
    "diff2": 0,
    "diff3": 0,
    "hour1": 0,  # Hours played on save.
    "hour2": 0,
    "hour3": 0,
    "min1": 0,  # Minutes played on save.
    "min2": 0,
    "min3": 0,
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
        base_path = f"{getenv("HOME")}/.wine/drive_c/users/{getenv("USER")}/AppData/Roaming/MMFApplications"
        self.spath = f"{base_path}/fnafw{self.slot}"
        self.ipath = "%s/info" %base_path

  def validate(self, _controller) -> None:
    """
    Check if the current save and info files exist.
    If not, create the file(s).

    Later, maybe write default data to the save, and delete the file
    if no changes end up being made.
    """

    if not exists(self.spath):
      _controller.warn(f"{self.spath} not found, but will be made now.")
      with open(self.spath, "x") as f: f.write("")

    if not exists(self.ipath):
      _controller.warn(f"{self.ipath} not found, but will be made now.")
      with open(self.ipath, "x") as f: f.write("")

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

  def read_all(self, _controller) -> tuple[dict[str, int], dict[str, int]]:
    """
    Reads the entire save & info file into `self.sdata` and `self.idata`.
    """

    with open(self.spath, 'r') as sfile:
      for i, line in enumerate(lines:=sfile.readlines()):
        # https://regex101.com/r/ZL10bq/1
        if match(r"[a-z0-9]+=[0-9]+", line):
          name, value = line.split('=')

          if name not in self.sdata: self.raise_bad_property(_controller, name, i)
          else: self.sdata[name] = int(value)

      print(self.sdata)
      return (self.sdata, self.idata)

    with open(self.ipath, 'r') as sfile: ...

  def read_char_data(self, _controller) -> tuple[dict[str, int], dict[str, int]]: ...

  def prettify(self, _controller) -> None: ...
  def reset(self, _controller) -> None: ...

  def raise_bad_property(self, _controller, _bad_property: str, _i: int) -> None:
    _controller.err(f"'{_bad_property}' is not a known property ({self.spath}:{_i+1}).")
