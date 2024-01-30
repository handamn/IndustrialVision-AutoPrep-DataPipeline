import os
import shutil


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
            train_artefact_folder = folder.replace("1_Stock_Photo", "2_Train_Artefact")
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
