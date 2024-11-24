#!/bin/bash

# Compiles FWTools GUI and CLI into `bin/<os>`.
os=$(uname -s | tr A-Z a-z)
bin="bin/$os"
exename="FWTools"
guipath="src/gui.py"
clipath="src/cli.py"

# Attempt to mkdir `bin` & `bin/<os>`.
function mkbin() {
  echo "Making 'bin' & 'bin/$os'..."
  mkdir -p "bin"
  mkdir -p $bin
}

# Compile `src/gui.py`.
function compilegui() {
  echo "Compiling 'src/gui.py'..."
  pyinstaller --onefile --add-data "assets/logos/FWToolslogo.png;assets/logos" --distpath $bin --name $exename $guipath
}

# Compile `src/cli.py`.
function compilecli() {
  echo "Compiling 'src/cli.py'..."
  pyinstaller --onefile --distpath $bin --name $exename-cli $clipath
}

function cleanup() {
  rm FWTools-cli.spec
  rm FWTools.spec
  rm -r build
}

mkbin
compilegui
compilecli
cleanup
echo "Done!"
