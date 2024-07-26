import os
import shutil
from pathlib import Path


def organiser(directory):
    org_path = Path().resolve().as_posix() + "/organised-files/"
    file_name = os.listdir(directory)
    folder_name = ['txt files', 'word doc files', 'spreadsheets']
    txt_file_dir = "txt files/"
    word_doc_dir = "word doc files/"
    spreadsheet_dir = "spreadsheets/"

    # create directory for organised files
    if not os.path.exists(org_path):
        os.makedirs(org_path)

    # create organised files in organised directory
    for i in range(0, len(folder_name)):
        if not os.path.exists(org_path + folder_name[i]):
            os.makedirs(org_path + folder_name[i])

    # move each file type to its respective folder
    for i in range(0, len(file_name)):
        for j in file_name:
            if ".txt" in j and not os.path.exists(org_path + txt_file_dir + j):
                shutil.copy(directory + j, org_path + txt_file_dir + j)
                # ^ using .copy for demo purposes, should be replaced with .move
            elif ".docx" in j and not os.path.exists(org_path + word_doc_dir + j):
                shutil.copy(directory + j, org_path + word_doc_dir + j)
            elif ".xlsx" in j and not os.path.exists(org_path + spreadsheet_dir + j):
                shutil.copy(directory + j, org_path + spreadsheet_dir + j)


directory_to_organise = Path().resolve().as_posix() + "/files/File/"
organiser(directory_to_organise)
