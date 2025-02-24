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
# Function to move files into categorized folders
def organize_files():
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Identify file type and move it
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                destination = os.path.join(DOWNLOADS_FOLDER, category, filename)
                shutil.move(file_path, destination)
                print(f"Moved: {filename} → {category}")
                break

# Run the file organizer
organize_files()
print("File organization completed!")
 
