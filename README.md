# PDF Compressor

A user-friendly desktop application for compressing PDF files while maintaining reasonable quality. Built with Python and Tkinter.

## Features

- Simple and intuitive graphical user interface
- Multiple compression quality options:
  - Screen (Maximum compression, ~60-90% reduction)
  - Ebook (Good compression, ~50-80% reduction)
  - Printer (Medium compression, ~30-50% reduction)
  - Prepress (High quality, ~10-30% reduction)
- Automatic file naming to prevent overwriting existing files
- Real-time compression progress indicator
- Detailed compression results showing original and final sizes

## Requirements

- Windows Operating System
- Python 3.6 or higher
- Ghostscript (included in the release package)
- Required Python packages:
  ```
  tkinter (usually comes with Python)
  ```

## Installation

### Method 1: Using the Executable (Recommended)
1. Download the latest release from the [Releases](https://github.com/yourusername/PDF-Compressor/releases) page
2. Extract the ZIP file
3. Run `PDF-Compressor.exe`

### Method 2: From Source
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/PDF-Compressor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PDF-Compressor
   ```
3. Install Ghostscript:
   - Download from [Ghostscript official website](https://www.ghostscript.com/releases/gsdnld.html)
   - Install and ensure it's in your system PATH, or
   - Place the required files (`gswin64c.exe` and `gsdll64.dll`) in the `gs/bin` folder

4. Run the application:
   ```bash
   python pdf_compressor.py
   ```

## Usage

1. Launch the application
2. Click "Browse" to select your PDF file
3. Choose your desired compression quality:
   - Screen: Best for viewing on screen, highest compression
   - Ebook: Good for e-readers, balanced compression
   - Printer: Suitable for regular printing
   - Prepress: High quality, minimal compression
4. Click "Compress PDF"
5. Wait for the compression to complete
6. The compressed file will be saved with "_compressed" suffix in the same directory

## File Naming Convention

- Compressed files are automatically named with the suffix "_compressed"
- If a file with the same name exists, a number is added (e.g., `document_compressed_1.pdf`)

## Troubleshooting

### Common Issues:

1. **"Ghostscript files not found" error**
   - Ensure Ghostscript is properly installed
   - Check if `gswin64c.exe` and `gsdll64.dll` are present in the `gs/bin` folder

2. **Application won't start**
   - Verify Python is installed correctly
   - Ensure all dependencies are met
   - Check if you have sufficient permissions

3. **Compression fails**
   - Verify the input PDF is not corrupted
   - Ensure you have write permissions in the output directory
   - Check if the PDF is not password-protected

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using [Ghostscript](https://www.ghostscript.com/) for PDF compression
- Icon and UI design by SPK

## Author

SPK - [GitHub Profile] (https://github.com/parvez144)

---

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
