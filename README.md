# PDF Compressor

A professional desktop application to compress PDF files while maintaining reasonable quality. Developed by Shahriar Parvez.

## Features
- Easy-to-use graphical interface
- Select PDF files through a file browser
- Compress PDFs while maintaining readability
- Supports most PDF file formats
- Professional installer with proper Windows integration
- Desktop and Start Menu shortcuts
- Proper uninstaller
- No file size limitations
- Custom application icon

## Installation
1. Download the `PDF_Compressor_Setup.exe` installer
2. Run the installer and follow the on-screen instructions
3. Choose whether to create a desktop shortcut
4. The application will be installed in your Program Files directory

## Usage
1. Launch the application from the Start Menu or desktop shortcut
2. Click the "Select File" button to choose a PDF file
3. Choose your desired compression quality:
   - Screen (maximum compression)
   - Ebook (good compression)
   - Printer (medium compression)
   - Prepress (high quality)
4. Click "Compress PDF"
5. The compressed file will be saved in the same location as the original file with "_compressed" added to the filename

## System Requirements
- Windows 10 or later
- No additional software required - all necessary components are included
- Administrator rights are not required for installation

## Antivirus Information
This application may trigger antivirus warnings because it bundles all necessary components into a single executable. This is a common false positive with PyInstaller-created applications. The application is completely safe to use and does not contain any malicious code.

If you receive an antivirus warning:
1. You can safely add the application to your antivirus exclusion list
2. The source code is available for review if needed
3. The application has been built with proper version information and metadata

## Notes
- The original PDF file will not be modified
- The compressed version will be saved as a new file
- Compression ratio may vary depending on the content of the PDF
- For best results, use PDFs with text and images
- The application includes Ghostscript for PDF processing

## Support
For any issues or questions, please contact:
- Developer: Shahriar Parvez
- Version: 1.0.0
- Copyright © 2024

## For Developers: Building the Application

### Prerequisites
1. Python 3.x installed
2. Required Python packages:
   - PyInstaller
   - Ghostscript (system dependency)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Build the Executable with PyInstaller
1. Create the spec file:
   ```bash
   pyi-makespec --onefile --windowed --icon=spk.ico pdf_compressor.py
   ```

2. Edit the spec file to include Ghostscript:
   - Add Ghostscript binaries to the binaries list
   - Add the icon file to the datas list

3. Build the executable:
   ```bash
   pyinstaller pdf_compressor.spec
   ```

4. Verify the executable:
   - Check `dist/PDF_Compressor.exe`
   - Test the executable
   - Ensure Ghostscript is working

### Step 3: Create the Setup with Inno Setup
1. Install Inno Setup (Download from: https://jrsoftware.org/isdl.php)

2. Prepare your files:
   - `dist/PDF_Compressor.exe` (PyInstaller executable)
   - `spk.ico` (Application icon)
   - `setup.iss` (Inno Setup script)

3. Open Inno Setup Compiler:
   - Launch Inno Setup Compiler
   - Open the `setup.iss` file
   - Click "Compile" (or press F9)
   - The setup file will be created in the `Output` folder

4. Verify the setup:
   - Test the setup on your computer
   - Check all functionality
   - Ensure proper Windows integration

### Troubleshooting

#### PyInstaller Issues
- If executable doesn't run, check Ghostscript inclusion
- If size is too large, check for unnecessary files
- If antivirus triggers, verify the build process

#### Inno Setup Issues
- If setup creation fails, verify all required files exist
- If setup size is too large, check PyInstaller executable size
- Ensure proper file paths in setup.iss 
