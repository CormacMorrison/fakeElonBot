#!/bin/bash
# Define the virtual environment directory name
VENV_DIR="$HOME/fakeElonBot"

if ! python3 -m venv --help > /dev/null 2>&1; then
    echo "'venv' module is not available. Installing python3-venv..."
    sudo apt-get install python3-venv -y || pip install virtualenv
    echo "'venv' module installed."
fi
# Check if virtual environment directory exists
if [ ! -f "$VENV_DIR/pyvenv.cfg" ]; then
    echo "Virtual environment not found, creating one..."
    
    # Create virtual environment
    python3 -m venv $VENV_DIR
    
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

echo "Virtual environment activated."