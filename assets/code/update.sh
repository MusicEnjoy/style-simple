#!/bin/bash

# Navigate to the style-simple directory
cd $HOME/style-simple || exit

# Pull the latest changes from the remote repository
git pull origin main

# Provide feedback to the user
echo "Repository updated successfully!"