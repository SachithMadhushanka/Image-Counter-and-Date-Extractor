# Image Counter and Date Extractor

## Overview

The Image Counter and Date Extractor is a Python-based desktop application that allows users to count image files in a selected folder, extract their modification dates, and rename the images in ascending order based on their modification dates. The application provides a simple graphical user interface (GUI) for browsing and selecting the folder containing the images.

## Features

- Browse and select a folder containing images.
- Count the total number of image files in the selected folder.
- Extract and display the modification dates of the images.
- Rename the images in ascending order based on their modification dates.

## Requirements

- Python 3.x
- tkinter

## Installation

1. **Install the required Python packages:**
   ```bash
   pip install tkinter
   ```

## Usage

1. **Run the application:**
   ```bash
   python image_counter_date_extractor.py
   ```

2. **Use the application:**
   - Click the "Browse Folder" button to select a folder containing images.
   - The application will count the total number of images, extract their modification dates, and rename the images in ascending order based on the dates.
   - The total number of images and their modification dates will be displayed in the application window.

## Script Explanation

### Importing Libraries
```python
import os
from tkinter import filedialog, Tk, Label, Button
from datetime import datetime
```
- **os**: For interacting with the operating system.
- **filedialog**: For opening a folder selection dialog.
- **Tk, Label, Button**: For creating the GUI components.
- **datetime**: For handling and formatting dates.

### Function to Count Images and Extract Dates
```python
def count_images_and_dates(folder_path):
    image_count = 0
    image_info = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_count += 1
            try:
                modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                image_info.append((file_name, modified_time))
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

    return image_count, image_info
```
- Counts the number of image files and extracts their modification dates.

### Function to Rename Images
```python
def rename_images(folder_path, image_info):
    image_info.sort(key=lambda x: x[1])  # Sort image_info based on modified time
    for i, (old_name, _) in enumerate(image_info):
        _, ext = os.path.splitext(old_name)
        new_name = f"{i+1}{ext}"  # Rename files in ascending order
        os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))
```
- Renames images in ascending order based on their modification dates.

### Function to Browse Folder
```python
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        image_count, image_info = count_images_and_dates(folder_path)
        rename_images(folder_path, image_info)
        update_display(image_count, image_info)
```
- Opens a folder selection dialog and processes the selected folder.

### Function to Update Display
```python
def update_display(image_count, image_info):
    info_label.config(text=f"Total Images: {image_count}\n\nImage Info:\n" + '\n'.join(f"{name}: {date}" for name, date in image_info))
```
- Updates the GUI with the total number of images and their modification dates.

### Creating the GUI
```python
# GUI setup
root = Tk()
root.title("Image Counter and Date Extractor")

browse_button = Button(root, text="Browse Folder", command=browse_folder)
browse_button.pack(pady=10)

info_label = Label(root, text="")
info_label.pack()

root.mainloop()
```
- Sets up the main window and GUI components for browsing folders and displaying image information.

## License

This project is licensed under the MIT License.
