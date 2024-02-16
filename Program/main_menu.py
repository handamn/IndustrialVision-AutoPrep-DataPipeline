import os
import sys
import Start5_2___all_function___V4 as funct
import Start4_5___master2___V18 as foldering

ground_folder = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
project_folder = ground_folder + "\\Project"
program_folder = ground_folder + "\\Program"

print(ground_folder)

print("1. New Project")
print("2. Load Project")

decision = int(input("Enter Menu : "))
if decision == 1:
    print(" ===== Create Project ===== ")
    print("")
    foldering.master_program(project_folder)

elif decision == 2:
    print("Files and Directories in " + project_folder + " : ")

    dir_list = os.listdir(project_folder)
    print(dir_list)
    print("")

    pick_folder = str(input("Choose Project Name : "))
    print("currently in the folder " + pick_folder)

    base_folder_menu_1 = project_folder + "\\" + pick_folder + "\\"

    print(base_folder_menu_1)

    pick_menu = funct.print_menu()

    if pick_menu == "1":
        funct.capture(base_folder_menu_1)
    
    elif pick_menu == "2":
        funct.pick_rand(base_folder_menu_1)
    
    elif pick_menu == "3":
        funct.labeling(base_folder_menu_1)
    
    elif pick_menu == "4":
        funct.train(base_folder_menu_1, program_folder)