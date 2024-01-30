import os
import shutil
import Start4_folder_V1 as foldering

def print_menu():
    print("\nProgram Generator\n")
    print("Pilih Menu :")
    print("1. Ambil Gambar")
    print("2. Pilih Random 50")
    print("3. Anotasi")
    print("4. Training Prepare Image")
    print("5. Auto Anotasi")
    print("6. Combine")
    print("7. Training Final\n")

    hasil_menu    = input("Enter Menu                                       : ")
    # Clear screen command
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================================")

    return hasil_menu

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\Project\\"

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

    foldering.create_folders(os.path.join(BASIS_FOLDER, nama_project), isi_kedalaman, folder_names, BASIS_FOLDER)

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

    pilih_menu = print_menu()

    if pilih_menu == "1":
        print("UHUYYYY")


