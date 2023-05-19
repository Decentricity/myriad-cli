#!/bin/bash

# Check if wget is installed
if ! command -v wget &>/dev/null; then
    echo "wget not found. Attempting to install..."
    sudo apt-get update
    sudo apt-get install wget
fi

# Check if ~/myriad/ directory exists and create it if not
if [ ! -d "$HOME/myriad" ]; then
  mkdir $HOME/myriad
fi

# Change into the ~/myriad/ directory
cd $HOME/myriad

# Download files
wget https://raw.githubusercontent.com/Decentricity/myriad-cli/main/myriad-cli
wget https://raw.githubusercontent.com/Decentricity/myriad-cli/main/myriad-cli.py

# Make files executable
chmod +x myriad-cli
chmod +x myriad-cli.py

# Add the directory to PATH in .bashrc if it's not already there
grep -qxF 'export PATH=$HOME/myriad:$PATH' $HOME/.bashrc || echo 'export PATH=$HOME/myriad:$PATH' >> $HOME/.bashrc

# Source .bashrc to update the current shell
source $HOME/.bashrc

echo "myriad-cli is now installed. You can run it with the command: myriad-cli."
echo "If this does not work, close and reopen your terminal session."
