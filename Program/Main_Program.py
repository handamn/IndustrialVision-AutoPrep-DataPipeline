import os

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\Project\\"

def create_folders(folder_name, folder_depths, folder_names, current_depth=0):
    if current_depth == len(folder_depths):
        """os.makedirs(os.path.join(folder_name, "images"))
        os.makedirs(os.path.join(folder_name, "labels"))
        os.makedirs(os.path.join(folder_name, "X_Automasi"))
        os.makedirs(os.path.join(folder_name, "models"))
        os.makedirs(os.path.join(folder_name, "X_Automasi", "images"))
        os.makedirs(os.path.join(folder_name, "X_Automasi", "labels"))"""
        return
    
    for i in range(folder_depths[current_depth]):
        subfolder_name = os.path.join(BASIS_FOLDER,folder_name, folder_names[current_depth][i])
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
    ####################
    print("Buat Project")
    print("")
    ####################
    nama_project = input("Masukkan Nama Project : ")
    print("")

    kedalaman = input("Masukkan Kedalaman Folder : ")
    isi_kedalaman = []
    for i in range(0,int(kedalaman)):
        item = int(input(f"Masukkan jumlah subfolder untuk tingkat kedalaman {i+1}: "))
        isi_kedalaman.append(item)

        subfolders = []
        #num_subfolders = int(input(f"Masukkan jumlah subfolder untuk tingkat kedalaman {i+1}: "))
        # Loop untuk setiap subfolder pada tingkat kedalaman tertentu
        for j in range(item):
            subfolder_name = input(f"Masukkan nama subfolder {j+1} pada tingkat kedalaman {i+1}: ")
            subfolders.append(subfolder_name)
        
        # Menambahkan list subfolder ke dalam list utama
        folder_names.append(subfolders)        

    create_folders(nama_project, isi_kedalaman, folder_names)