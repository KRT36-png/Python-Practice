import os 
import shutil
from pathlib import Path
Original_Directory=input("Enter the File directory path:")
files = [f for f in os.listdir(Original_Directory) if os.path.isfile(os.path.join(Original_Directory, f))]
images_folder_create_location= Original_Directory + "/Images"
Audios_folder_create_location= Original_Directory + "/Audio"
documents_folder_create_location= Original_Directory + "/Documents"
Videos_folder_create_location= Original_Directory + "/Videos"
Others_folder_create_location= Original_Directory + "/Others"
os.makedirs(images_folder_create_location, exist_ok=True)
os.makedirs(Audios_folder_create_location, exist_ok=True)
os.makedirs(documents_folder_create_location, exist_ok=True)
os.makedirs(Videos_folder_create_location, exist_ok=True)
os.makedirs(Others_folder_create_location, exist_ok=True)
for i in range(len(files)):
    source_file_path=os.path.join(Original_Directory, files[i])
    if ".jpg" == (Path(files[i])).suffix.lower():
        shutil.move(source_file_path,os.path.join(images_folder_create_location, files[i]))
    elif ".mp3" == (Path(files[i])).suffix.lower():
        shutil.move(source_file_path,os.path.join(Audios_folder_create_location, files[i]))
    elif ".pdf" == (Path(files[i])).suffix.lower():
        shutil.move(source_file_path,os.path.join(documents_folder_create_location, files[i]))
    elif ".mp4" == (Path(files[i])).suffix.lower():
        shutil.move(source_file_path,os.path.join(Videos_folder_create_location, files[i]))
    else:
        shutil.move(source_file_path,os.path.join(Others_folder_create_location, files[i]))
