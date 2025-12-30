@echo off
title Assessment Sheet Extractor
color 0A

echo.
echo ============================================================
echo          ASSESSMENT SHEET EXTRACTOR
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo [ERROR] Python is not installed!
    echo.
    echo Please download and install Python 3.8 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo During installation, make sure to check:
    echo  [X] Add Python to PATH
    echo.
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version
echo.

REM Check if running in virtual environment
if defined VIRTUAL_ENV (
    echo [OK] Virtual environment is active
) else (
    REM Check if venv exists
    if exist "venv\Scripts\activate.bat" (
        echo [*] Activating virtual environment...
        call venv\Scripts\activate.bat
    ) else (
        echo [*] Creating virtual environment...
        python -m venv venv
        if errorlevel 1 (
            color 0C
            echo [ERROR] Failed to create virtual environment
            pause
            exit /b 1
        )
        call venv\Scripts\activate.bat
    )
)

echo.
echo [*] Checking dependencies...

REM Quick check if streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo [*] Installing required packages (this may take 1-2 minutes)...
    echo.
    python -m pip install --upgrade pip >nul 2>&1
    pip install -r requirements.txt
    if errorlevel 1 (
        color 0C
        echo.
        echo [ERROR] Failed to install dependencies
        echo.
        pause
        exit /b 1
    )
    echo.
    echo [OK] All dependencies installed successfully!
) else (
    echo [OK] Dependencies already installed
)

echo.
echo ============================================================
echo              STARTING APPLICATION...
echo ============================================================
echo.
echo The application will open in your web browser shortly.
echo.
echo URL: http://localhost:8501
echo.
echo To stop the application:
echo  - Press Ctrl+C in this window
echo  - Or close this window
echo.
echo ============================================================
echo.

REM Start Streamlit
streamlit run app.py

REM If streamlit exits, pause so user can see any errors
if errorlevel 1 (
    echo.
    echo ============================================================
    echo [ERROR] Application stopped with errors
    echo ============================================================
    pause
)
