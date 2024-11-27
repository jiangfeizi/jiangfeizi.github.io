import os
import shutil

dir_path = r'C:\Users\11310\Downloads\20241126'

for item in os.listdir(dir_path):
    rename = item.replace('.crdownload', '')
    shutil.move(os.path.join(dir_path, item), os.path.join(dir_path, rename))