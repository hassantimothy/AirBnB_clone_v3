#!/bin/bash

# Source environment setup script
source setup_env.sh

# Execute your command
python3 -m unittest discover tests
