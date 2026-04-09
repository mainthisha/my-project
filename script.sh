#!/bin/bash

# Take input path
read -p "Enter the path: " path

# Check conditions
if [ -f "$path" ]; then
    echo "It is a File"
elif [ -d "$path" ]; then
    echo "It is a Directory"
else
    echo "Path does not exist"
fi