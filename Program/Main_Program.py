import os
import shutil

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\Project\\"

def create_folders(folder_name, folder_depths, folder_names, current_depth=0, is_folder_A=True):
    if current_depth == 0:
        project_folder = os.path.join(BASIS_FOLDER, folder_name)
        os.makedirs(project_folder)
        
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(project_folder, "1_Stock_Photo", folder_names[current_depth][i])
            os.makedirs(subfolder_name)
            create_folders(subfolder_name, folder_depths, folder_names, current_depth + 1, is_folder_A=True)
            train_artefact_folder = folder_name.replace("1_Stock_Photo", "2_Train_Artefact")
            os.makedirs(train_artefact_folder)
            duplicate_structure(subfolder_name, train_artefact_folder)
    
    elif current_depth < len(folder_depths) - 1:
        for i in range(folder_depths[current_depth]):
            subfolder_name = os.path.join(folder_name, folder_names[current_depth][i])
            os.makedirs(subfolder_name)
            create_folders(subfolder_name, folder_depths, folder_names, current_depth + 1, is_folder_A)

def duplicate_structure(source_folder, target_folder):
    for root, dirs, files in os.walk(source_folder):
        for dir_name in dirs:
            os.makedirs(os.path.join(root.replace(source_folder, target_folder), dir_name))

        for root, dirs, files in os.walk(target_folder):
            for item in ["images", "labels", "X_Automasi"]:
                if item in dirs:
                    shutil.rmtree(os.path.join(root, item))

        for root, dirs, files in os.walk(target_folder):
            if not dirs:
                for item in ["train", "val", "test", "models"]:
                    os.makedirs(os.path.join(root, item))
                    os.makedirs(os.path.join(root, item, "images"))
                    os.makedirs(os.path.join(root, item, "labels"))

############################################
def run_python_file(file_name, arguments=None):
    try:
        subprocess.run(["python", file_name] + (arguments or []), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
############################################

# Clear screen command
os.system('cls' if os.name == 'nt' else 'clear')

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
