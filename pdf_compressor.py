import os
import subprocess
import sys
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class PDFCompressor:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.validate_ghostscript()  # Validate on startup

    def setup_ui(self):
        self.root.title("PDF Compressor")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#2D2D2D")
        
        # Try to set icon
        try:
            icon_path = self.get_icon_path()
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Warning: Could not set icon: {str(e)}")
            
        # Header
        tk.Label(self.root, text="Select a PDF File:", 
                bg="#2D2D2D", fg="white", font=("Helvetica", 12, "bold")).pack(pady=5)

        # Input field
        self.input_entry = tk.Entry(self.root, bg="#F0F0F0", width=60)
        self.input_entry.pack(padx=10, pady=5)

        # Browse button
        tk.Button(self.root, text="Browse", command=self.browse_file,
                 bg="#008080", fg="white", font=("Inter", 12, "bold")).pack(pady=5)

        # Quality selection
        tk.Label(self.root, text="Select Compression Quality:",
                bg="#2D2D2D", fg="white", font=("Helvetica", 11, "bold")).pack(pady=5)

        self.quality_var = tk.StringVar(value="screen (max compression, ~60-90%)")
        quality_options = [
            "screen (max compression, ~60-90%)",
            "ebook (good compression, ~50-80%)",
            "printer (medium compression, ~30-50%)",
            "prepress (high quality, ~10-30%)"
        ]
        quality_dropdown = ttk.Combobox(self.root, textvariable=self.quality_var, 
                                      values=quality_options, font=("Helvetica", 11),
                                      state="readonly", width=40)
        quality_dropdown.pack(pady=5)

        # Info label
        tk.Label(self.root, 
                 text="ℹ️ This tool compresses your PDF,\nQuality affects size & clarity.\n'screen' = smallest size, 'prepress' = highest quality.\nUse based on your need.",
                 bg="white", fg="black", font=("Helvetica", 9, "italic")).pack(pady=10)

        # Compress button
        self.compress_btn = tk.Button(self.root, text="Compress PDF", 
                                    command=self.start_compression, bg="#2c3e50", 
                                    fg="white", font=("inter", 12, "bold"), 
                                    padx=20, pady=5, state=tk.NORMAL)
        self.compress_btn.pack(pady=15)

        # Progress bar (hidden initially)
        self.progress = ttk.Progressbar(self.root, mode='indeterminate', length=300)
        
        # Status label
        self.status_label = tk.Label(self.root, text="", bg="#2D2D2D", fg="white")
        self.status_label.pack(pady=5)
        
        # Footer
        footer_label = tk.Label(self.root, text="© 2024 | by spk", 
                              bg="#2D2D2D", font=("inter", 8, "italic"), fg="white")
        footer_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    def get_icon_path(self):
        """Get path to icon file, works for both development and packaged app"""
        try:
            base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            icon_path = os.path.join(base_dir, "spk.ico")
            if not os.path.exists(icon_path):
                # Try alternative paths if needed
                icon_path = os.path.join(os.path.dirname(sys.executable), "spk.ico")
            return icon_path
        except Exception as e:
            print(f"Warning: Could not find icon: {str(e)}")
            return None

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, file_path)

    def validate_ghostscript(self):
        """Check if Ghostscript is available with all required files"""
        try:
            base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            gs_path = os.path.join(base_dir, "gs", "bin", "gswin64c.exe")
            gs_dll = os.path.join(base_dir, "gs", "bin", "gsdll64.dll")
            
            # Try alternative path if not found
            if not os.path.exists(gs_path):
                gs_path = os.path.join(os.path.dirname(sys.executable), "gs", "bin", "gswin64c.exe")
                gs_dll = os.path.join(os.path.dirname(sys.executable), "gs", "bin", "gsdll64.dll")
            
            if not (os.path.exists(gs_path) and os.path.exists(gs_dll)):
                messagebox.showerror("Error", 
                                   "Ghostscript files not found.\nPlease ensure gswin64c.exe and gsdll64.dll are in the 'gs/bin' folder.\n\n"
                                   "You can download Ghostscript from: https://www.ghostscript.com/releases/gsdnld.html")
                return False
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Ghostscript validation failed: {str(e)}")
            return False

    def get_output_path(self, input_path):
        """Generate output path that doesn't overwrite existing files"""
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_compressed{ext}"
        counter = 1
        
        while os.path.exists(output_path):
            output_path = f"{base}_compressed_{counter}{ext}"
            counter += 1
            
        return output_path

    def get_file_size(self, path):
        """Get file size in MB"""
        return os.path.getsize(path) / (1024 * 1024)

    def compress_pdf(self, input_path, output_path, quality_label):
        if not self.validate_ghostscript():
            return False

        quality_map = {
            "screen (max compression, ~60-90%)": "screen",
            "ebook (good compression, ~50-80%)": "ebook",
            "printer (medium compression, ~30-50%)": "printer",
            "prepress (high quality, ~10-30%)": "prepress"
        }
        quality = quality_map.get(quality_label, "screen")
        
        base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        gs_path = os.path.join(base_dir, "gs", "bin", "gswin64c.exe")
        
        # Try alternative path if not found
        if not os.path.exists(gs_path):
            gs_path = os.path.join(os.path.dirname(sys.executable), "gs", "bin", "gswin64c.exe")

        # Handle paths with spaces
        if ' ' in input_path:
            input_path = f'"{input_path}"'
        if ' ' in output_path:
            output_path = f'"{output_path}"'

        gs_command = [
            gs_path,  
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS=/{quality}",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_path}",
            input_path
        ]

        try:
            # Show progress
            self.progress.pack(pady=10)
            self.progress.start()
            self.compress_btn.config(state=tk.DISABLED)
            self.status_label.config(text="Compressing PDF...")
            self.root.update()
            
            # Get original file size
            original_size = self.get_file_size(input_path.strip('"'))
            
            # Run compression (handle spaces in paths)
            if sys.platform == 'win32':
                subprocess.run(' '.join(gs_command), shell=True, check=True)
            else:
                subprocess.run(gs_command, check=True)
            
            # Get compressed file size
            compressed_size = self.get_file_size(output_path.strip('"'))
            compression_ratio = (1 - (compressed_size / original_size)) * 100
            
            # Success message with compression ratio
            messagebox.showinfo("Success", 
                              f"✅ Compressed PDF saved at:\n{output_path}\n\n"
                              f"Original size: {original_size:.2f} MB\n"
                              f"Compressed size: {compressed_size:.2f} MB\n"
                              f"Compression ratio: {compression_ratio:.1f}%")
            return True
            
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"❌ Compression failed:\n{e}")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"❌ An unexpected error occurred:\n{str(e)}")
            return False
        finally:
            self.progress.stop()
            self.progress.pack_forget()
            self.compress_btn.config(state=tk.NORMAL)
            self.status_label.config(text="")

    def start_compression(self):
        input_path = self.input_entry.get().strip()
        
        if not input_path:
            messagebox.showwarning("Warning", "Please select a PDF file first.")
            return

        if not os.path.isfile(input_path):
            messagebox.showwarning("Warning", "The specified file does not exist.")
            return

        if not input_path.lower().endswith('.pdf'):
            messagebox.showwarning("Warning", "Please select a valid PDF file.")
            return

        output_path = self.get_output_path(input_path)
        quality_label = self.quality_var.get()
        
        self.compress_pdf(input_path, output_path, quality_label)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFCompressor(root)
    root.mainloop() 
