#!/bin/bash

set -e

echo "Setting up Flask backend..."

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cat > .env << EOF
PORT=3001
FRONTEND_URL=http://localhost:3000
DEBUG=True
FLASK_ENV=development
EOF
    echo ".env file created. Please review and update if needed."
fi

echo "Starting Flask development server..."
python app.py

