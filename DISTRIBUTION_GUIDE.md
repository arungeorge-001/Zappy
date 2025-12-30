# Assessment Sheet Extractor - Distribution Guide

## Option 1: Portable Package (Recommended for Non-Technical Users)

### What to Share:
Share the entire folder containing:
- `install_and_run.bat` - Double-click launcher
- `app.py` - Main application
- `pdf_extractor.py` - PDF processing logic
- `requirements.txt` - Dependencies list
- `README.md` - User guide

### Requirements for Users:
Users need to have **Python 3.8 or higher** installed:
- Download from: https://www.python.org/downloads/
- During installation, check "Add Python to PATH"

### How Users Run It:
1. Extract the folder to any location
2. Double-click `install_and_run.bat`
3. First run: Automatically installs dependencies
4. Application opens in web browser
5. Upload PDF and process

### Advantages:
- Small package size (~50KB)
- Easy to update (just replace files)
- Users can see the source code
- Works on any Windows with Python

---

## Option 2: Standalone Executable (Easiest for End Users)

### What to Share:
- `AssessmentExtractor.exe` (from `dist` folder)
- Sample PDF (optional)
- Quick start instructions

### Requirements for Users:
- None (fully standalone)

### How Users Run It:
1. Double-click `AssessmentExtractor.exe`
2. Application opens in web browser
3. Upload PDF and process

### Advantages:
- No Python installation needed
- Single file distribution
- True "double-click and run"

### Disadvantages:
- Large file size (~500MB-1GB due to bundled Python)
- Takes longer to start up
- Antivirus may flag it

---

## Option 3: Cloud Deployment (Best for Multiple Users)

### Platforms:
1. **Streamlit Cloud** (Free):
   - Push code to GitHub
   - Connect at https://streamlit.io/cloud
   - Get shareable URL

2. **Heroku** (Free tier available)
3. **AWS/Azure/GCP** (Paid)

### Advantages:
- No installation for users
- Access from any device
- Centralized updates
- Works on Mac/Linux/Windows

---

## Creating the Portable Package

### Step 1: Create a ZIP file
1. Create a new folder called `AssessmentExtractor_Portable`
2. Copy these files into it:
   - `install_and_run.bat`
   - `app.py`
   - `pdf_extractor.py`
   - `requirements.txt`
   - `README.md`
   - (Optional) Sample PDF file

3. Right-click the folder → "Send to" → "Compressed (zipped) folder"

### Step 2: Share
- Email the ZIP file
- Upload to Google Drive/Dropbox
- Share via USB drive

---

## For the Standalone EXE

### After Building:
1. Navigate to the `dist` folder
2. Find `AssessmentExtractor.exe`
3. Test it first on your machine
4. Compress it to ZIP (optional)
5. Share the EXE

### Note on Antivirus:
Some antivirus software may flag PyInstaller executables as suspicious because:
- They're not digitally signed
- They unpack code at runtime

**Solution**: Get a code signing certificate or use Option 1 instead.

---

## Recommended Distribution Method

**For General Users**: Option 1 (Portable Package)
- Small size
- Easy to verify source code
- No antivirus issues
- Users just need Python

**For Non-Technical Users**: Option 2 (EXE)
- No installation required
- Just double-click to run

**For Multiple Users/Organization**: Option 3 (Cloud)
- Central access point
- No distribution needed
- Easy updates

---

## Quick Start Guide to Include

```
ASSESSMENT SHEET EXTRACTOR
Quick Start Guide

1. FIRST TIME SETUP:
   - Ensure Python 3.8+ is installed
   - Double-click "install_and_run.bat"
   - Wait for dependencies to install

2. USING THE APPLICATION:
   - Application opens in your web browser
   - Click "Browse files" to select PDF
   - Click "Process File"
   - Review the extracted data
   - Click "Download Excel File"

3. TROUBLESHOOTING:
   - If Python not found: Install from python.org
   - If browser doesn't open: Visit http://localhost:8501
   - If errors occur: Check that PDF follows expected format

4. SUPPORT:
   - Email: [your-email@example.com]
   - Check README.md for detailed instructions
```

---

## File Checklist for Distribution

### Portable Package:
- [ ] install_and_run.bat
- [ ] app.py
- [ ] pdf_extractor.py
- [ ] requirements.txt
- [ ] README.md
- [ ] QUICK_START.txt (optional)
- [ ] Sample PDF (optional)

### Standalone EXE:
- [ ] AssessmentExtractor.exe
- [ ] QUICK_START.txt
- [ ] Sample PDF (optional)

---

## Version Updates

When updating the application:

**Portable Package**:
- Replace `app.py` and/or `pdf_extractor.py`
- Update `requirements.txt` if needed
- Users just replace files and re-run

**Standalone EXE**:
- Rebuild with PyInstaller
- Replace the entire EXE file

**Cloud**:
- Push updates to repository
- Automatic deployment
