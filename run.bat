@echo off
color 0f

:: Installing App Requirements
echo . . .
python --version
echo . . . 
pip install -r requirements.txt
echo . . . 
echo . . . 
:: Run Application Command
set DEBUG=1 && python main.py
::pause
exit