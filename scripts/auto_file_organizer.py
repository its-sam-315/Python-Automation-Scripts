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
 
