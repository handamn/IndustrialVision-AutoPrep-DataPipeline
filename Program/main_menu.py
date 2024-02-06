import os
import shutil
import funct_foldering as foldering
import funct_all_function as functioning

base_folder = "F:\\repo_generator\\V1\\data_generator\\Project\\"

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

def write_text(project_name, list_name):
    file_name = os.path.join(base_folder, project_name) + "\group.txt"
    with open(file_name, 'w+') as f:
        for items in list_name:
            f.write('%s\n' %items)
    f.close()

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
    group = []
    x = 0
    for i in range(0, int(kedalaman)):
        print("")
        group_folder = input(f"Masukkan nama grouping folder tingkat kedalaman {i+1}: ")
        group.append(group_folder)
        item = int(input(f"Masukkan jumlah subfolder untuk tingkat kedalaman {i+1}: "))
        isi_kedalaman.append(item)

        subfolders = []
        for j in range(item):
            subfolder_name = input(f"Masukkan nama subfolder {j+1} untuk folder {nama_project}: ")
            subfolders.append(subfolder_name)

        folder_names.append(subfolders)
        x+=1
    
    print("")
    coba = input(f"Masukkan nama grouping folder tingkat kedalaman {x+1}: ")
    group.append(coba)

    foldering.create_folders(os.path.join(base_folder, nama_project), isi_kedalaman, folder_names, base_folder)
    write_text(nama_project, group)

    crop = input("potong dimana? :")

    indeks = group.index(crop)

    foldering.cut_folder(nama_project, len(group), indeks)


elif int(decision) == 2:
    dir_list = os.listdir(base_folder) 

    print("Files and directories in '", base_folder, "' :") 

    # print the list 
    print(dir_list)

    print("")
    
    pilih_folder = input("Masukkan Nama Project : ")
    print("Saat ini sedang di project " + pilih_folder)

    base_folder_menu_1 = base_folder + pilih_folder + "\\"

    pilih_menu = print_menu()

    if pilih_menu == "1":
        functioning.capture(base_folder_menu_1)
    
    elif pilih_menu == "2":
        functioning.pick_rand(base_folder_menu_1)
    
    elif pilih_menu == "3":
        functioning.labeling(base_folder_menu_1)
    
    elif pilih_menu == "4":
        print("")