import os
import csv
from datetime import datetime

def scan_drive(drive_path, output_file):
    print(f"Scanning drive: {drive_path}")
    
    # Open the CSV file with utf-8 encoding
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Add headers for file name, file path, size, and date modified
        writer.writerow(['File Name', 'File Path', 'File Size (MB)', 'Date Modified'])

        found_files = False  # Flag to check if any files were found

        for root, dirs, files in os.walk(drive_path):
            print(f"Accessing directory: {root}")  # Debug output
            for name in files:
                full_path = os.path.join(root, name)
                # Get file size in MB and last modified date
                file_size = os.path.getsize(full_path) / (1024 * 1024)  # Convert size to MB
                last_modified = os.path.getmtime(full_path)
                last_modified_date = datetime.fromtimestamp(last_modified).strftime('%Y-%m-%d %H:%M:%S')

                # Write file details to CSV
                writer.writerow([name, full_path, round(file_size, 2), last_modified_date])
                found_files = True
                print(f"Found file: {name} at {full_path} (Size: {round(file_size, 2)} MB, Modified: {last_modified_date})")

        if not found_files:
            print("No files found in the specified drive.")

    print(f"Scan complete. Output saved to {output_file}")

# Use UNC path to access the network drive
scan_drive(r"D:\\", r"c:\drive_data\video_media.csv")
