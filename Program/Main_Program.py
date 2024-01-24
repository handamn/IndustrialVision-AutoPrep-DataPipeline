import os
import shutil

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\Project\\"

def create_folders(folder_name, folder_depths, folder_names, current_depth=0, is_folder_A=True):
    
    if current_depth == 0:  # Menambahkan pembuatan folder nama project, folder_A, dan folder_B
        project_folder = os.path.join(BASIS_FOLDER, folder_name)
        os.makedirs(project_folder)
        os.makedirs(os.path.join(project_folder, "folder_A"))
        
        # Memasukkan kedalaman folder dan subfolder ke dalam folder_A
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(project_folder, "folder_A", folder_names[current_depth][i])
            os.makedirs(subfolder_name)  # Membuat subfolder
            create_folders(subfolder_name, folder_depths, folder_names, current_depth + 1, is_folder_A=True)
    
    elif current_depth == len(folder_depths) - 1:
        last_subfolder_names = []
        for i in range(folder_depths[current_depth]):
            num_subfolders = int(input(f"Masukkan jumlah subfolder untuk folder {folder_names[current_depth][i]}: "))
            names = []
            for j in range(num_subfolders):
                name = input(f"Masukkan nama subfolder {j+1} untuk folder {folder_name[len(BASIS_FOLDER):]} {folder_names[current_depth][i]}: ")
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
                    pass  # Tidak melakukan pembuatan folder untuk folder_B
    
    elif current_depth < len(folder_depths) - 1:  # Periksa apakah sudah mencapai kedalaman terakhir
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(folder_name, folder_names[current_depth][i])
            os.makedirs(subfolder_name)  # Membuat folder
            create_folders(subfolder_name, folder_depths, folder_names, current_depth + 1, is_folder_A)
    
    # Setelah proses pembuatan struktur folder_A selesai, salin struktur folder_A ke folder_B
    if current_depth == 0 and is_folder_A:
        folder_A_path = os.path.join(BASIS_FOLDER, folder_name, "folder_A")
        folder_B_path = os.path.join(BASIS_FOLDER, folder_name, "folder_B")
        shutil.copytree(folder_A_path, folder_B_path)





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

elif int(decision) == 2:
    dir_list = os.listdir(BASIS_FOLDER) 

    print("Files and directories in '", BASIS_FOLDER, "' :") 

    # print the list 
    print(dir_list)

    print("")
    
    pilih_folder = input("Masukkan Nama Project : ")
    print("Saat ini sedang di project " + pilih_folder)

    BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\Project\\" + pilih_folder + "\\"

    print(BASIS_FOLDER)
