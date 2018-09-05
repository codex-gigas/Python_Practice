import os
import string
def rename_files():
    file_list = os.listdir(r"T:\PyProjects\sec_messg")
    saved_path = os.getcwd()
    print(saved_path)
    change_path = os.chdir(r"T:\PyProjects\sec_messg")
    print(change_path)
    for file_name in file_list:
        print("old name- " + file_name)
        
        print("New name- " + file_name.translate(None, "0123456789"))
        os.rename(file_name,file_name.translate(None, "0123456789"))
        os.chdir(saved_path)

rename_files()
