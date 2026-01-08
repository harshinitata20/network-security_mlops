@echo off
echo Starting Network Security MLOps Project Setup...

REM Create conda environment
echo Creating conda environment...
conda create -p venv python=3.10 -y

REM Activate environment
echo Activating environment...
call conda activate venv/

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create .env file if not exists
if not exist .env (
    echo Creating .env file from example...
    copy .env.example .env
    echo Please update .env file with your MongoDB connection string
)

echo Setup completed!
echo Next steps:
echo 1. Update .env file with your MongoDB URL
echo 2. Run 'python push_data.py' to push data to MongoDB
echo 3. Run 'python main.py' to train the model
echo 4. Run 'python app.py' to start the API server

pause
