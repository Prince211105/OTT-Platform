@echo off
rem Install and update project dependencies, then apply migrations

rem Change to project directory
cd /d "%~dp0"

rem Create virtual environment if it does not exist
if not exist venv (python -m venv venv)

rem Activate virtual environment
call venv\Scripts\activate.bat

rem Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

rem Apply database migrations
python manage.py migrate

echo Dependencies installed and migrations applied.
