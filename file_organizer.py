import os
import shutil
import json

MAIN_FOLDER = r"D:\Download\Downloads_test"
SCRIPT_NAME = 'file_organizer.py'
OTHERS_CATEGORY = 'Others'
CATEGORIES_FILE = 'categories.json'
LOG_FILE_NAME = "organizer_log.txt"


with open(CATEGORIES_FILE, "r") as f:
    CATEGORIES_DICT = json.load(f)

def organize_files(folder_path):
    log_file = os.path.join(folder_path, LOG_FILE_NAME)

    for category in list(CATEGORIES_DICT.keys())+[OTHERS_CATEGORY]:
        folder_path_category = os.path.join(folder_path,category)
        if not os.path.exists(folder_path_category):
            os.makedirs(folder_path_category)

    all_files = []

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path ,item)
        if os.path.isfile(full_path) and os.path.basename(full_path) != SCRIPT_NAME and os.path.basename(full_path) != "file_organizer_gui.py":
            all_files.append(full_path)


    for file in all_files:
        file_name = os.path.basename(file)
        base,ext = os.path.splitext(file_name)
        ext = ext.lower()
        moved = False

        for category,extensions in CATEGORIES_DICT.items():
            if ext in extensions:
                dest_path = os.path.join(folder_path, category, file_name)
                counter = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(folder_path, category, f"{base}({counter}){ext}")
                    counter += 1

                shutil.move(file, dest_path)
                with open(log_file, "a") as log:
                    log.write(f"{file_name} --> {category}\n")

                moved = True
                break
        if not moved:
            dest_path = os.path.join(folder_path, OTHERS_CATEGORY, file_name)
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(folder_path, OTHERS_CATEGORY, f"{base}({counter}){ext}")
                counter += 1
            shutil.move(file, dest_path)
            with open(log_file, "a") as log:
                log.write(f"{file_name} --> {OTHERS_CATEGORY}\n")

if __name__ == '__main__':
    organize_files(MAIN_FOLDER)
    print("✅ File Organizer completed!")