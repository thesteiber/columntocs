import csv
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from pathlib import Path
import os
import shutil

class CSVConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Convert Column to Comma Separated")
        self.root.geometry("500x200")
        
        # Create temp directory if it doesn't exist
        self.temp_dir = Path("temp")
        self.temp_dir.mkdir(exist_ok=True)
        
        # Create main frame with padding
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input file selection
        ttk.Label(main_frame, text="Input CSV File:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.input_path = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.input_path, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_input).grid(row=0, column=2)
        
        # Quote type selection
        ttk.Label(main_frame, text="Quote Type:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.quote_type = tk.StringVar(value="none")
        quote_frame = ttk.Frame(main_frame)
        quote_frame.grid(row=1, column=1, sticky=tk.W)
        ttk.Radiobutton(quote_frame, text="No Quotes", variable=self.quote_type, value="none").pack(side=tk.LEFT)
        ttk.Radiobutton(quote_frame, text="Single Quotes", variable=self.quote_type, value="single").pack(side=tk.LEFT)
        ttk.Radiobutton(quote_frame, text="Double Quotes", variable=self.quote_type, value="double").pack(side=tk.LEFT)
        
        # Convert button
        ttk.Button(main_frame, text="Convert", command=self.convert).grid(row=2, column=0, columnspan=3, pady=20)
        
        # Status label
        self.status_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_var).grid(row=3, column=0, columnspan=3)

    def browse_input(self):
        filename = filedialog.askopenfilename(
            title="Select Input CSV File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if filename:
            self.input_path.set(filename)

    def convert(self):
        input_file = self.input_path.get()
        
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        
        try:
            # Read the CSV file
            with open(input_file, 'r', encoding='utf-8') as csvfile:
                values = [row[0] for row in csv.reader(csvfile)]
            
            # Process the values based on quote type
            quote_type = self.quote_type.get()
            if quote_type == 'single':
                processed_values = [f"'{value}'" for value in values]
            elif quote_type == 'double':
                processed_values = [f'"{value}"' for value in values]
            else:
                processed_values = values
            
            # Create temp output file
            input_filename = Path(input_file).stem
            temp_output = self.temp_dir / f"{input_filename}_converted.txt"
            
            # Write to temp file
            with open(temp_output, 'w', encoding='utf-8') as txtfile:
                txtfile.write(','.join(processed_values))
            
            # Prompt user to save the file
            save_filename = filedialog.asksaveasfilename(
                title="Save Converted File As",
                initialfile=f"{input_filename}_converted.txt",
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            
            if save_filename:
                # Copy the temp file to the user's chosen location
                shutil.copy2(temp_output, save_filename)
                # Clean up temp file
                temp_output.unlink()
                
                # Update status with just filenames
                input_filename = Path(input_file).name
                output_filename = Path(save_filename).name
                self.status_var.set(f"Successfully converted {input_filename} to {output_filename}")
                messagebox.showinfo("Success", "Conversion completed successfully!")
            else:
                # If user cancels save dialog, clean up temp file
                temp_output.unlink()
                self.status_var.set("Conversion cancelled")
            
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
            # Clean up temp file if it exists
            if 'temp_output' in locals() and temp_output.exists():
                temp_output.unlink()

def main():
    root = tk.Tk()
    app = CSVConverterGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main() 