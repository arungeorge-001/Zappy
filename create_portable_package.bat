@echo off
echo ============================================
echo Creating Portable Package
echo ============================================
echo.

REM Create package directory
set PACKAGE_DIR=AssessmentExtractor_Portable
if exist "%PACKAGE_DIR%" rmdir /s /q "%PACKAGE_DIR%"
mkdir "%PACKAGE_DIR%"

echo Copying files...

REM Copy application files
copy "install_and_run.bat" "%PACKAGE_DIR%\" >nul
copy "app.py" "%PACKAGE_DIR%\" >nul
copy "pdf_extractor.py" "%PACKAGE_DIR%\" >nul
copy "requirements.txt" "%PACKAGE_DIR%\" >nul
copy "README.md" "%PACKAGE_DIR%\" >nul
copy "QUICK_START.txt" "%PACKAGE_DIR%\" >nul

REM Copy sample PDF if exists
if exist "Mukesh Kumar S_AssessmentSheet.pdf" (
    echo Copying sample PDF...
    copy "Mukesh Kumar S_AssessmentSheet.pdf" "%PACKAGE_DIR%\Sample_Assessment.pdf" >nul
)

echo.
echo ============================================
echo Package created successfully!
echo ============================================
echo.
echo Location: %CD%\%PACKAGE_DIR%
echo.
echo Next steps:
echo 1. Review the contents in the %PACKAGE_DIR% folder
echo 2. Create a ZIP file of this folder
echo 3. Share the ZIP file with others
echo.
echo Files included:
dir "%PACKAGE_DIR%" /b
echo.
echo To create ZIP manually:
echo - Right-click the folder
echo - Select "Send to" ^> "Compressed (zipped) folder"
echo.

pause
