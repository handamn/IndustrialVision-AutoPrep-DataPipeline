import os
import sys

##############################
def Create_Dir_Base(value_list, current_combination=[]):
    #os.mkdir(script_directory + project_location)
    if not value_list:
        path_create = script_directory + project_location + "\\" + Name_Project + "\\" + "\\".join(current_combination)
        print(path_create)
        #os.mkdir(path_create)

    else:
        for item in value_list[0]:
            Create_Dir_Base(value_list[1:], current_combination + [item])


def Store_Dir_Base(value_list, current_combination=[]):
    if not value_list:
        # Base case: If value_list is empty, return the current combination
        return "\\".join(current_combination)
    else:
        combinations = []
        # Recursive case: Iterate through each item in the current list and call the function recursively
        for item in value_list[0]:
            combinations.append(Store_Dir_Base(value_list[1:], current_combination + [item]))
        return combinations

def display_list_recursive(lst):
    if isinstance(lst, list):
        for item in lst:
            display_list_recursive(item)
    else:
        print(lst)


def flatten_list(main_list):
    flat = []
    for sublist in main_list:
        for item in sublist:
            flat.extend(item)
    
    return flat



##############################


script_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

directory_dict = {}

project_location = "\\Project"


Name_Project = str(input("Enter Name Project : "))
Folder_Depth = int(input("Enter Folder Depth : "))

for i in range(Folder_Depth - 1):
    Name_Group = str(input("Enter Grouping Name for depth " + str(i+1) + " : "))
    count_subfolder = int(input("Enter How Much Subfolder for " + Name_Group + " : "))

    sub_folder = []

    for j in range (count_subfolder):
        Name_Sub = str(input("Enter Sub Name for " + Name_Group + " Sub " + str(j+1) + " : "))
        sub_folder.append(Name_Sub)

    directory_dict[Name_Group] = sub_folder


key_list = list(directory_dict.keys())
value_list = list(directory_dict.values())

Create_Dir_list = []

for i in range(len(value_list)):
    if i+1 == len(value_list):
        print("masuk disini")
        print("")
        Create_Dir_list.append(value_list[i])
        Create_Dir_Base(Create_Dir_list)
        print("")

    else:
        print("")
        Create_Dir_list.append(value_list[i])
        Create_Dir_Base(Create_Dir_list)
        print("")

Storing_Group_Name = Store_Dir_Base(value_list)

print(value_list)


sub_folder = {}
key_sub_folder = flatten_list(Storing_Group_Name)

for i in range(len(key_sub_folder)):
    count_subfolder_2 = int(input("Enter How Much Subfolder for " + key_sub_folder[i] +" : "))

    sub_folder_2 = []

    for j in range(count_subfolder_2):
        Name_Sub_2 = str(input("Enter Sub Name for " + key_sub_folder[i] + " -" + str(j) + "- : "))
        sub_folder_2.append(Name_Sub_2)
    
    sub_folder[key_sub_folder[i]] = sub_folder_2


print(sub_folder)
print("")
print(value_list)

