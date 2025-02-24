import os
import shutil

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

# Get the directory to organize
DOWNLOADS_FOLDER = os.path.expanduser("~") + "\\Downloads"

# Ensure categorized folders exist
for category in FILE_CATEGORIES.keys():
    category_path = os.path.join(DOWNLOADS_FOLDER, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

print("Folders set up successfully!")
# Function to move files into categorized folders with error handling
def organize_files():
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                destination_folder = os.path.join(DOWNLOADS_FOLDER, category)
                destination = os.path.join(destination_folder, filename)

                # Handle duplicate file names
                counter = 1
                while os.path.exists(destination):
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_{counter}{ext}"
                    destination = os.path.join(destination_folder, new_filename)
                    counter += 1

                shutil.move(file_path, destination)
                print(f"Moved: {filename} → {category}")
                moved = True
                break

        # Move unknown files to "Miscellaneous"
        if not moved:
            misc_folder = os.path.join(DOWNLOADS_FOLDER, "Miscellaneous")
            if not os.path.exists(misc_folder):
                os.makedirs(misc_folder)
            shutil.move(file_path, os.path.join(misc_folder, filename))
            print(f"Moved: {filename} → Miscellaneous")

# Run the improved file organizer
organize_files()
print("File organization completed successfully!")
