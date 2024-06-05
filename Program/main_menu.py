import os
import shutil
import funct_foldering as foldering
import funct_all_function as functioning

base_folder = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))) + "\\Project"

print("1. New Project")
print("2. Load Project")

decision = int(input("Enter Menu : "))
if decision == 1:
    print(" ===== Create Project ===== ")
    print("")
    foldering.master_program(base_folder)

elif decision == 2:
    print("Files and Directories in " + base_folder + " : ")

    dir_list = os.listdir(base_folder)
    print(dir_list)
    print("")

    pick_folder = str(input("Choose Project Name : "))
    print("currently in the folder " + pick_folder)

    base_folder_menu_1 = base_folder + "\\" + pick_folder + "\\"
    
    pick_menu = funct.print_menu()

    if pick_menu == "1":
        funct.capture(base_folder_menu_1)
    
    elif pick_menu == "2":
        funct.pick_rand(base_folder_menu_1)
    
    elif pick_menu == "3":
        funct.labeling(base_folder_menu_1)