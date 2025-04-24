import zipfile
import os

# Path to your ZIP file and where you want to extract
zip_path  = r"C:\Users\gpkt2\OneDrive\Desktop\job_assignment\DATA SCIENTIST_ASSIGNMENT-20250423T114630Z-001\DATA SCIENTIST_ASSIGNMENT\Licplatesdetection_train.zip"
extract_to =r"C:\Users\gpkt2\OneDrive\Desktop\job_assignment\DATA SCIENTIST_ASSIGNMENT-20250423T114630Z-001\DATA SCIENTIST_ASSIGNMENT\Licplatesdetection_train"

# Extract
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Extraction complete.")
