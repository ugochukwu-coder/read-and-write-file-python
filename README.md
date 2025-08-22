# File Read & Write Utility

## Overview
The `file_read_write()` function reads a text file, modifies its content (converts everything to uppercase), and writes the modified version to a new file.

It also allows the user to choose where the new file should be saved:
- In the same folder as the input file  
- In a custom folder specified by the user  

## Features
- Reads text files with UTF-8 encoding  
- Ignores problematic characters (`errors="ignore"`)  
- Saves modified content as a new file prefixed with `modified_`  
- Lets the user choose the save location (same folder or custom path)  
- Handles errors gracefully:
  - File not found  
  - Permission denied  
  - Unexpected runtime errors  

## Function Definition
```python
import os

def file_read_write():
    # Ask user for input file
    filename = input("Enter the filename to read: ").strip()

    try:
        # Try to open and read the file with utf-8 encoding
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Modify the content (example: uppercase)
        modified_content = content.upper()

        # Ask user where to save
        choice = input("Save in the same folder? (y/n): ").strip().lower()

        if choice == "y":
            # Save in same folder
            new_filename = "modified_" + os.path.basename(filename)
        else:
            # Ask for custom folder
            folder = input("Enter the folder path to save in: ").strip()

            # Ensure folder exists
            if not os.path.exists(folder):
                print("❌ Error: That folder does not exist.")
                return

            # Create new file path in custom folder
            new_filename = os.path.join(folder, "modified_" + os.path.basename(filename))

        # Write modified content to new file with utf-8 encoding
        with open(new_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(modified_content)

        print(f"✅ File has been successfully written to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don't have permission to read/write this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
