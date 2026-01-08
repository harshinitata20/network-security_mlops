#!/bin/bash

echo "Starting Network Security MLOps Project Setup..."

# Create conda environment
echo "Creating conda environment..."
conda create -p venv python=3.10 -y

# Activate environment
echo "Activating environment..."
source activate ./venv

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if not exists
if [ ! -f .env ]; then
    echo "Creating .env file from example..."
    cp .env.example .env
    echo "Please update .env file with your MongoDB connection string"
fi

echo "Setup completed!"
echo "Next steps:"
echo "1. Update .env file with your MongoDB URL"
echo "2. Run 'python push_data.py' to push data to MongoDB"
echo "3. Run 'python main.py' to train the model"
echo "4. Run 'python app.py' to start the API server"
