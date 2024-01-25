import os

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\Project\\"

def create_folders(folder_name, folder_depths, folder_names, current_depth=0, is_folder_A=True):
    
    if current_depth == 0:  # Menambahkan pembuatan folder nama project, 1_Stock_Photo, dan 2_Train_Artefact
        project_folder = os.path.join(BASIS_FOLDER, folder_name)
        os.makedirs(project_folder)
        os.makedirs(os.path.join(project_folder, "1_Stock_Photo"))
        os.makedirs(os.path.join(project_folder, "2_Train_Artefact"))
        
        # Memasukkan kedalaman folder dan subfolder ke dalam 1_Stock_Photo
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(project_folder, "1_Stock_Photo", folder_names[current_depth][i])
            os.makedirs(subfolder_name)  # Membuat subfolder
            create_folders(subfolder_name, folder_depths, folder_names, current_depth + 1, is_folder_A=True)
        
        # Memasukkan kedalaman folder dan subfolder ke dalam 2_Train_Artefact
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(project_folder, "2_Train_Artefact", folder_names[current_depth][i])
            os.makedirs(subfolder_name)  # Membuat subfolder
            create_folders(subfolder_name, folder_depths, folder_names, current_depth + 1, is_folder_A=False)
    
    elif current_depth == len(folder_depths) - 1:
        for i in range(folder_depths[current_depth]):
            subfolder_name_1 = os.path.join(folder_name, folder_names[current_depth][i])
            os.makedirs(subfolder_name_1)  # Membuat folder

            subfolder_name_2 = os.path.join(folder_name.replace("1_Stock_Photo", "2_Train_Artefact"), folder_names[current_depth][i])
            os.makedirs(subfolder_name_2)  # Membuat folder
            
            # Menambahkan folder di subfolder terdalam
            os.makedirs(os.path.join(subfolder_name_1, "images"))
            os.makedirs(os.path.join(subfolder_name_1, "labels"))
            os.makedirs(os.path.join(subfolder_name_1, "X_Automasi"))
            os.makedirs(os.path.join(subfolder_name_1, "X_Automasi", "images"))
            os.makedirs(os.path.join(subfolder_name_1, "X_Automasi", "labels"))

            os.makedirs(os.path.join(subfolder_name_2, "gambar"))
            os.makedirs(os.path.join(subfolder_name_2, "tulisan"))
            os.makedirs(os.path.join(subfolder_name_2, "langsung"))
            os.makedirs(os.path.join(subfolder_name_2, "langsung", "gambar"))
            os.makedirs(os.path.join(subfolder_name_2, "langsung", "tulisan"))

    elif current_depth < len(folder_depths) - 1:  # Periksa apakah sudah mencapai kedalaman terakhir
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(folder_name, folder_names[current_depth][i])
            os.makedirs(subfolder_name)  # Membuat folder
            create_folders(subfolder_name, folder_depths, folder_names, current_depth + 1, is_folder_A)


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

    create_folders(os.path.join(BASIS_FOLDER, nama_project), isi_kedalaman, folder_names)

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
