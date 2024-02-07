import os
import random
import shutil
import yaml
import subprocess
import sys

def create_folders(folder_name, folder_depths, folder_names, BASE_FOLDER, current_depth=0, is_folder_A=True):
    if current_depth == 0:  # Menambahkan pembuatan folder nama project, 1_Stock_Photo, dan 2_Train_Artefact
        project_folder = os.path.join(BASE_FOLDER, folder_name)
        os.makedirs(project_folder)
        
        # Menyimpan struktur folder 1_Stock_Photo
        stock_photo_structure = []
        
        # Memasukkan kedalaman folder dan subfolder ke dalam 1_Stock_Photo
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(project_folder, "1_Stock_Photo", folder_names[current_depth][i])
            os.makedirs(subfolder_name)  # Membuat subfolder
            stock_photo_structure.append(subfolder_name)
            create_folders(subfolder_name, folder_depths, folder_names, BASE_FOLDER, current_depth + 1, is_folder_A=True)
        
        # Duplikasi struktur folder 1_Stock_Photo ke 2_Train_Artefact
        for folder in stock_photo_structure:
            train_artefact_folder = folder.replace("1_Stock_Photo", "3_Base")
            os.makedirs(train_artefact_folder)
            duplicate_structure(folder, train_artefact_folder)
    
    elif current_depth == len(folder_depths) - 1:
        last_subfolder_names = []
        for i in range(folder_depths[current_depth]):
            num_subfolders = int(input(f"Masukkan jumlah subfolder untuk folder {folder_names[current_depth][i]}: "))
            names = []
            for j in range(num_subfolders):
                name = input(f"Masukkan nama subfolder {j+1} untuk folder {folder_name[len(BASE_FOLDER):]} {folder_names[current_depth][i]}: ")
                names.append(name)
            last_subfolder_names.append(names)
        
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(folder_name, folder_names[current_depth][i])
            os.makedirs(subfolder_name)  # Membuat folder
            
            for name in last_subfolder_names[i]:
                if is_folder_A:
                    os.makedirs(os.path.join(subfolder_name, name, "images"))
                    os.makedirs(os.path.join(subfolder_name, name, "labels"))
                    os.makedirs(os.path.join(subfolder_name, name, "X_Automasi"))
                    os.makedirs(os.path.join(subfolder_name, name, "X_Automasi", "images"))
                    os.makedirs(os.path.join(subfolder_name, name, "X_Automasi", "labels"))
                else:
                    os.makedirs(os.path.join(subfolder_name, name, "train"))
                    os.makedirs(os.path.join(subfolder_name, name, "val"))
                    os.makedirs(os.path.join(subfolder_name, name, "test"))
                    os.makedirs(os.path.join(subfolder_name, name, "models"))
                    os.makedirs(os.path.join(subfolder_name, name, "train", "images"))
                    os.makedirs(os.path.join(subfolder_name, name, "train", "labels"))
                    os.makedirs(os.path.join(subfolder_name, name, "val", "images"))
                    os.makedirs(os.path.join(subfolder_name, name, "val", "labels"))
                    os.makedirs(os.path.join(subfolder_name, name, "test", "images"))
                    os.makedirs(os.path.join(subfolder_name, name, "test", "labels"))
    
    elif current_depth < len(folder_depths) - 1:  # Periksa apakah sudah mencapai kedalaman terakhir
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(folder_name, folder_names[current_depth][i])
            os.makedirs(subfolder_name)  # Membuat folder
            create_folders(subfolder_name, folder_depths, folder_names, BASE_FOLDER, current_depth + 1, is_folder_A)

def duplicate_structure(source_folder, target_folder):
    # Menyalin struktur folder dari sumber ke target
    for root, dirs, files in os.walk(source_folder):
        for dir_name in dirs:
            os.makedirs(os.path.join(root.replace(source_folder, target_folder), dir_name))

    # Menghapus folder images, labels, dan X_Automasi jika ada
    for root, dirs, files in os.walk(target_folder):
        if "images" in dirs:
            shutil.rmtree(os.path.join(root, "images"))
        if "labels" in dirs:
            shutil.rmtree(os.path.join(root, "labels"))
        if "X_Automasi" in dirs:
            shutil.rmtree(os.path.join(root, "X_Automasi"))

    for root, dirs, files in os.walk(target_folder):
        if not dirs:
            os.makedirs(os.path.join(root, "train"))
            os.makedirs(os.path.join(root, "train", "images"))
            os.makedirs(os.path.join(root, "train", "labels"))
            os.makedirs(os.path.join(root, "val"))
            os.makedirs(os.path.join(root, "val", "images"))
            os.makedirs(os.path.join(root, "val", "labels"))
            os.makedirs(os.path.join(root, "test"))
            os.makedirs(os.path.join(root, "test", "images"))
            os.makedirs(os.path.join(root, "test", "labels"))
            os.makedirs(os.path.join(root, "models"))


def list_all_subfolders_with_longest(path):
    subfolders = []
    max_depth = 0
    deepest_path = None
    for root, dirs, _ in os.walk(path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            subfolders.append(dir_path)
            # Update informasi tentang subfolder terdalam
            depth = len(os.path.relpath(dir_path, path).split(os.sep))
            if depth > max_depth:
                max_depth = depth
                deepest_path = dir_path

    parsed_deepest_path = deepest_path.split(os.sep)
    
    return subfolders, parsed_deepest_path


def copy_folder(name_project, group_len, index_group):
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    clean_script = script_directory.split('\\')
    base_route = ""
    for i in range(len(clean_script)):
        if clean_script[i] != "Program":
            if (i==0):
                base_route = clean_script[i]
            
            else :
                base_route += "\\" + clean_script[i]
    
    base_route += "\\" + "Project" + "\\" + name_project
    ground_route = base_route
    ground_route += "\\" + "3_Base"
    all_subfolders, deepest_path = list_all_subfolders_with_longest(ground_route)
    deepest_path_2 = deepest_path[: len(deepest_path) - 2]
    deepest_path_2 = deepest_path_2[- group_len:]
    copy_route = ground_route

    for i in range(0, index_group):
        copy_route += "\\" + deepest_path_2[i]

    dest_route = base_route
    dest_route += "\\" + "2_Train_artefact"
    delete_route = base_route
    delete_route += "\\" + "3_Base"

    shutil.copytree(copy_route, dest_route)
    #shutil.rmtree(delete_route)


def cut_folder(name_project):
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    clean_script = script_directory.split('\\')
    base_route = ""
    for i in range(len(clean_script)):
        if clean_script[i] != "Program":
            if (i==0):
                base_route = clean_script[i]
            
            else :
                base_route += "\\" + clean_script[i]
    
    base_route += "\\" + "Project" + "\\" + name_project

    delete_route = base_route
    delete_route += "\\" + "3_Base"

    shutil.rmtree(delete_route)