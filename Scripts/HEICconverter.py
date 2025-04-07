import os
from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIF/HEIC file handler
register_heif_opener()

# Ask user for input folder path
input_folder = input("Enter the input folder path: ").strip()

# Extract base path and last folder name to create the output path
base_path = os.path.dirname(os.path.dirname(input_folder))
last_folder_name = os.path.basename(input_folder)
output_folder = os.path.join(base_path, last_folder_name)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each file in the input folder
for file_name in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file_name)

    # Check for files with leading dot (e.g., ".filtered-...") and rename them
    if file_name.startswith('.') and '.' in file_name[1:]:
        new_name = file_name[1:]  # Remove the leading dot
        new_path = os.path.join(input_folder, new_name)
        os.rename(file_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")
        file_name = new_name  # Update file_name for further processing
        file_path = new_path

    # Convert HEIC to JPG
    if file_name.lower().endswith('.heic'):
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(output_folder, jpg_file_name)
        
        try:
            # Open HEIC image
            with Image.open(file_path) as img:
                # Save as JPG
                img.convert("RGB").save(jpg_file_path, "JPEG", quality=95)
            print(f"Converted: {file_name} -> {jpg_file_name}")
        except Exception as e:
            print(f"Failed to convert {file_name}: {e}")

print(f"Process completed. Converted files are saved in: {output_folder}")
