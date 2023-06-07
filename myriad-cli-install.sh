#!/bin/bash

echo "  .=++=:   :+++=."
echo " *=    =%*#-    =+     ::     .:                              ="
echo "++  .=+-  .=+=   #:    @@:   .%@:             =              +@"
echo "+=  ++-     -*-  #:    @%%.  %%@  %:  #  %++* %  +#+++%  *#++#@"
echo "+=    .=#**=.    #:    @#-%.#=-@   %.#   @    @  @=  =@ -@   *@"
echo "+=   -++: -++:   #:    @# +@* -@    @    @    @  %%==%@  %*-=%@"
echo "=*===:       :===%:                 #    "
echo ""
echo "Installing the Myriad.Social Command Line Interface client."

# Check if wget is installed
if ! command -v wget &>/dev/null; then
    echo "wget not found. Attempting to install..."
    sudo apt-get update
    sudo apt-get install wget -y
fi

# Check if ~/myriadclient/ directory exists and create it if not
if [ ! -d "$HOME/myriadclient" ]; then
  mkdir $HOME/myriadclient
fi

rm ~/myriadclient/*

# Change into the ~/myriadclient/ directory
cd $HOME/myriadclient

# Download files
wget --no-verbose https://raw.githubusercontent.com/Decentricity/myriad-cli/main/myriad-cli
wget --no-verbose https://raw.githubusercontent.com/Decentricity/myriad-cli/main/myriad-cli.py

# Make files executable
chmod +x myriad-cli
chmod +x myriad-cli.py

# Add the directory to PATH in .bashrc if it's not already there
grep -qxF 'export PATH=$HOME/myriadclient:$PATH' $HOME/.bashrc || echo 'export PATH=$HOME/myriadclient:$PATH' >> $HOME/.bashrc

# Source .bashrc to update the current shell
source $HOME/.bashrc

# Check if python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "python3 not found. Attempting to install..."
    sudo apt-get update
    sudo apt-get install python3 -y
fi

# Check if pip3 is installed
if ! command -v pip3 &>/dev/null; then
    echo "pip3 not found. Attempting to install..."
    sudo apt-get update
    sudo apt-get install python3-pip -y
fi

# Check if python3-tk is installed
if ! dpkg-query -W python3-tk; then
    echo "python3-tk not found. Attempting to install..."
    sudo apt-get update
    sudo apt-get install python3-tk -y
fi

# Check if python3-dev is installed
if ! dpkg-query -W python3-dev; then
    echo "python3-dev not found. Attempting to install..."
    sudo apt-get update
    sudo apt-get install python3-dev -y
fi

# List of python dependencies
declare -a arr=("requests" "pywhatkit" "pillow" "transformers" "torch")

for i in "${arr[@]}"
do
    pip_dependency=$(pip3 list | grep $i)
    if [ -z "$pip_dependency" ]; then
        echo "The $i module is not installed. Attempting to install..."
        pip3 install $i
    else
        echo ""
    fi
done
pip install art

echo "If there are no errors, myriad-cli is now in your path. You can run it with the command: "
echo "              myriad-cli"
echo ""
echo "If the command does not work, close and reopen your terminal session."
echo "If it still doesn't work, you can run the script directly by typing:"
echo "              ~/myriadclient/myriad-cli"
echo ""
echo "If you are still experiencing problems, you can rerun the curl script with sudo:"
echo "              curl -sSL https://myriad.social/cli | sudo bash"
