@echo off

call %~dp0"Bot\venv\Scripts\activate"

cd %~dp0Bot

set TOKEN="YOUR TOKEN"

python main.py

pause