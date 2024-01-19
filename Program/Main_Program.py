import os

def create_folders(folder_name, folder_depths, folder_names, current_depth=0):
    if current_depth == len(folder_depths):
        return
    
    for i in range(folder_depths[current_depth]):
        subfolder_name = os.path.join(folder_name, folder_names[current_depth][i])
        os.makedirs(subfolder_name)  # Membuat folder
        create_folders(subfolder_name, folder_depths, folder_names, current_depth + 1)

"""# Contoh pemanggilan fungsi
folder_name = 'MainFolder'
folder_depths = [2, 3, 2]  # Jumlah folder di setiap tingkat kedalaman
folder_names = [
    ['Subfolder_1_1', 'Subfolder_1_2'],
    ['Subfolder_2_1', 'Subfolder_2_2', 'Subfolder_2_3'],
    ['Subfolder_3_1', 'Subfolder_3_2']
]  # Nama folder di setiap tingkat kedalaman

create_folders(folder_name, folder_depths, folder_names)"""


# Clear screen command
os.system('cls' if os.name == 'nt' else 'clear')

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\"

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
        item = input("masukkan jumlah folder tingkat " + str(i+1) + " : ")
        isi_kedalaman.append(int(item))
        