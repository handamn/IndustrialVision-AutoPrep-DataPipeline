import os

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\Project\\"

def create_folders(folder_name, folder_depths, folder_names, current_depth=0):
    
    if current_depth == len(folder_depths) - 1:
        # If it's the last level, ask whether the last subfolder name should be the same for all folders
        same_last_subfolder = input("Apakah nama subfolder terakhir sama untuk semua folder? (y/n): ").lower().strip() == 'y'
        if same_last_subfolder:
            last_subfolder_name = input("Masukkan nama subfolder terakhir: ")
        else:
            last_subfolder_names = []
            for i in range(folder_depths[current_depth]):
                num_subfolders = int(input(f"Masukkan jumlah subfolder untuk folder {folder_names[current_depth][i]}: "))
                names = []
                for j in range(num_subfolders):
                    name = input(f"Masukkan nama subfolder {j+1} untuk folder {folder_name[len(BASIS_FOLDER):]} {folder_names[current_depth][i]}: ")
                    names.append(name)
                last_subfolder_names.append(names)
        
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(BASIS_FOLDER, folder_name, folder_names[current_depth][i])
            os.makedirs(subfolder_name)  # Membuat folder
            
            if same_last_subfolder:
                os.makedirs(os.path.join(subfolder_name, last_subfolder_name))
            else:
                for name in last_subfolder_names[i]:
                    os.makedirs(os.path.join(subfolder_name, name))
                    os.makedirs(os.path.join(subfolder_name, name, "images"))
                    os.makedirs(os.path.join(subfolder_name, name, "labels"))
                    os.makedirs(os.path.join(subfolder_name, name, "X_Automasi"))
                    os.makedirs(os.path.join(subfolder_name, name, "X_Automasi", "images"))
                    os.makedirs(os.path.join(subfolder_name, name, "X_Automasi", "labels"))
    
    elif current_depth < len(folder_depths) - 1:  # Periksa apakah sudah mencapai kedalaman terakhir
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(BASIS_FOLDER, folder_name, folder_names[current_depth][i])
            os.makedirs(subfolder_name)  # Membuat folder
            create_folders(subfolder_name, folder_depths, folder_names, current_depth + 1)

# Clear screen command
os.system('cls' if os.name == 'nt' else 'clear')

# Inisialisasi list kosong
folder_names = []

print("1. new project")
print("2. load project")

decision = input("Masukkan Menu : ")
if int(decision) == 1:
    print("Buat Project")
    print("")
    ####################
    nama_project = input("Masukkan Nama Project : ")
    print("")

    kedalaman = input("Masukkan Kedalaman Folder : ")
    isi_kedalaman = []
    for i in range(0, int(kedalaman)):
        item = int(input(f"Masukkan jumlah subfolder untuk tingkat kedalaman {i+1}: "))
        isi_kedalaman.append(item)

        subfolders = []
        for j in range(item):
            subfolder_name = input(f"Masukkan nama subfolder {j+1} untuk folder {nama_project}: ")
            subfolders.append(subfolder_name)
        
        folder_names.append(subfolders)        

    create_folders(nama_project, isi_kedalaman, folder_names)
