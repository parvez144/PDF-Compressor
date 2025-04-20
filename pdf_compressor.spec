# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None

# Add Ghostscript binaries directly
binaries = [
    ('gs/bin/gswin64c.exe', 'gs/bin'),
    ('gs/bin/gsdll64.dll', 'gs/bin')
]

# Define files to include
datas = [
    ('spk.ico', '.')  # Icon file
]

a = Analysis(
    ['pdf_compressor.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,  # Use the datas list we defined above
    hiddenimports=['tkinter', 'tkinter.ttk', 'tkinter.messagebox', 'tkinter.filedialog'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
    upx_exclude=[],
    upx=True,
    upx_compress_level=9,
    strip=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='spk.ico',
    version='file_version_info.txt'
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PDF_Compressor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='spk.ico'
) 