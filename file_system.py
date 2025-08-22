def file_read_write():
    # Ask user for input file
    filename = input("Enter the filename to read: ").strip()

    try:
        # Try to open and read the file with utf-8 encoding
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Modify the content (example: uppercase)
        modified_content = content.upper()

        # Create a new filename for the output
        new_filename = "modified_" + filename

        # Write modified content to new file with utf-8 encoding
        with open(new_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(modified_content)

        print(f" File has been successfully written to '{new_filename}'")

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print(" Error: You don't have permission to read/write this file.")
    except Exception as e:
        print(f" Unexpected error: {e}")


# Run the program
file_read_write()
