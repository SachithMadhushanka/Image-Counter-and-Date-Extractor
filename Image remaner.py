import os
from tkinter import filedialog, Tk, Label, Button
from datetime import datetime

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

def rename_images(folder_path, image_info):
    image_info.sort(key=lambda x: x[1])  # Sort image_info based on modified time
    for i, (old_name, _) in enumerate(image_info):
        _, ext = os.path.splitext(old_name)
        new_name = f"{i+1}{ext}"  # Rename files in ascending order
        os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        image_count, image_info = count_images_and_dates(folder_path)
        rename_images(folder_path, image_info)
        update_display(image_count, image_info)

def update_display(image_count, image_info):
    info_label.config(text=f"Total Images: {image_count}\n\nImage Info:\n" + '\n'.join(f"{name}: {date}" for name, date in image_info))

# GUI setup
root = Tk()
root.title("Image Counter and Date Extractor")

browse_button = Button(root, text="Browse Folder", command=browse_folder)
browse_button.pack(pady=10)

info_label = Label(root, text="")
info_label.pack()

root.mainloop()
