@echo off
REM Set UTF-8 code page
chcp 65001

REM Start a new CMD window and run the Python script
start cmd /k python "%~dp0main.py"
