#!/bin/bash

# Check if wget is installed
if ! command -v wget &>/dev/null; then
    echo "wget not found. Attempting to install..."
    sudo apt-get update
    sudo apt-get install wget
fi

# Check if ~/myriad-client/ directory exists and create it if not
if [ ! -d "~/myriad-client" ]; then
  mkdir ~/myriad-client
fi

# Change into the ~/myriad-client/ directory
cd ~/myriad-client

# Download files
wget https://raw.githubusercontent.com/Decentricity/myriad-cli/main/myriad-cli
wget https://raw.githubusercontent.com/Decentricity/myriad-cli/main/myriad-cli.py

# Make files executable
chmod +x myriad-cli
chmod +x myriad-cli.py

# Run the script
./myriad-cli

