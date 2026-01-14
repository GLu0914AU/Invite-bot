#!/bin/bash

# Where Winds Meet Invite Bot Startup Script

echo "Starting Where Winds Meet Invite Bot..."

# Check if .env exists
if [ ! -f .env ]; then
    echo "Error: .env file not found!"
    echo "Please copy .env.example to .env and configure it."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed!"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
python3 -c "import discord" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Run the bot
echo "Starting bot..."
python3 bot.py
