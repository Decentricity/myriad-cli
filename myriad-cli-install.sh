#!/bin/bash

# Check if wget is installed
if ! command -v wget &>/dev/null; then
    echo "wget not found. Attempting to install..."
    sudo apt-get update
    sudo apt-get install wget
fi

# Check if ~/myriadclient/ directory exists and create it if not
if [ ! -d "$HOME/myriadclient" ]; then
  mkdir $HOME/myriadclient
fi

# Change into the ~/myriadclient/ directory
cd $HOME/myriadclient

# Download files
wget https://raw.githubusercontent.com/Decentricity/myriad-cli/main/myriad-cli
wget https://raw.githubusercontent.com/Decentricity/myriad-cli/main/myriad-cli.py

# Make files executable
chmod +x myriad-cli
chmod +x myriad-cli.py

# Add the directory to PATH in .bashrc if it's not already there
grep -qxF 'export PATH=$HOME/myriadclient:$PATH' $HOME/.bashrc || echo 'export PATH=$HOME/myriadclient:$PATH' >> $HOME/.bashrc

# Source .bashrc to update the current shell
source $HOME/.bashrc

echo "myriad-cli is now in your path. You can run it with the command: myriad-cli."
echo "If the command does not work, close and reopen your terminal session."
