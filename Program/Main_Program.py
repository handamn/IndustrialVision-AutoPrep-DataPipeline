import os

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\Project\\"

def create_folders_recursive(folder_path, folder_depths, folder_names, current_depth=0):
    if current_depth == len(folder_depths):
        return
    
    for folder_name in folder_names[current_depth]:
        subfolder_path = os.path.join(folder_path, folder_name)
        os.makedirs(subfolder_path)  # Membuat folder
        if current_depth == len(folder_depths) - 1:
            create_last_subfolders(subfolder_path)
        else:
            create_folders_recursive(subfolder_path, folder_depths, folder_names, current_depth + 1)

def create_last_subfolders(folder_path):
    num_subfolders = int(input("Masukkan jumlah subfolder: "))
    for _ in range(num_subfolders):
        subfolder_name = input("Masukkan nama subfolder: ")
        subfolder_path = os.path.join(folder_path, subfolder_name)
        os.makedirs(subfolder_path)  # Membuat folder
        create_subfolders_inside_last(subfolder_path)

def create_subfolders_inside_last(subfolder_path):
    subfolders = ["images", "labels", "X_Automasi", "X_Automasi/images", "X_Automasi/labels"]
    for subfolder in subfolders:
        os.makedirs(os.path.join(subfolder_path, subfolder))

def main():
    # Clear screen command
    os.system('cls' if os.name == 'nt' else 'clear')

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
        folder_names = []  # Definisi folder_names di sini
        for i in range(0, int(kedalaman)):
            item = int(input(f"Masukkan jumlah subfolder untuk tingkat kedalaman {i+1}: "))
            isi_kedalaman.append(item)

            subfolders = []
            for j in range(item):
                subfolder_name = input(f"Masukkan nama subfolder {j+1} untuk folder {nama_project}: ")
                subfolders.append(subfolder_name)

            folder_names.append(subfolders)

        create_folders_recursive(os.path.join(BASIS_FOLDER, nama_project), isi_kedalaman, folder_names)

if __name__ == "__main__":
    main()
