import os
import sys

##############################
def Create_Dir_Base(branch, value_list, current_combination=[]):
    #os.mkdir(script_directory + project_location)
    if not value_list:
        path_create = script_directory + project_location + "\\" + Name_Project + "\\" + branch + "\\" + "\\".join(current_combination)
        print(path_create)
        #os.mkdir(path_create)

    else:
        for item in value_list[0]:
            Create_Dir_Base(branch, value_list[1:], current_combination + [item])


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


def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

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

Length_Folder_Depth = 1
for i in range(len(value_list)):
    Length_Folder_Depth *= len(value_list[i])



potong = str(input("potong dimana : "))
ind = int(key_list.index(potong))

new_value_list = value_list[ind+1:]

Length_Folder_Depth_2 = 1
for i in range(len(new_value_list)):
    Length_Folder_Depth_2 *= len(new_value_list[i])



Create_Dir_list = []

for i in range(len(value_list)):
    if i+1 == len(value_list):
        print("masuk disini")
        print("")
        Create_Dir_list.append(value_list[i])
        Create_Dir_Base("1_Stock_Photo",Create_Dir_list)
        print("")

    else:
        print("")
        Create_Dir_list.append(value_list[i])
        Create_Dir_Base("1_Stock_Photo",Create_Dir_list)
        print("")

Storing_Group_Name = Store_Dir_Base(value_list)


Create_Dir_list_2 = []

for i in range(len(new_value_list)):
    if i+1 == len(new_value_list):
        print("masuk disini")
        print("")
        Create_Dir_list_2.append(new_value_list[i])
        Create_Dir_Base("2_Train_Artefact", Create_Dir_list_2)
        print("")
    
    else:
        print("")
        Create_Dir_list_2.append(new_value_list[i])
        Create_Dir_Base("2_Train_Artefact", Create_Dir_list_2)

Storing_Group_Name_2 = Store_Dir_Base(new_value_list)



A_sub_folder = {}
B_sub_folder = {}
key_sub_folder = flatten_list(Storing_Group_Name)
key_sub_folder_2 = flatten_list(Storing_Group_Name_2)


for i in range(Length_Folder_Depth):
    count_subfolder_2 = int(input("Enter How Much Subfolder for " + key_sub_folder[i] +" : "))

    sub_folder_2 = []
    sub_folder_2a = []

    for j in range(count_subfolder_2):
        Name_Sub_2 = str(input("Enter Sub Name for " + key_sub_folder[i] + " -" + str(j) + "- : "))
        sub_folder_2.append(Name_Sub_2)

        if (i+1) > (Length_Folder_Depth-Length_Folder_Depth_2):
            sub_folder_2a.append(Name_Sub_2)
    
    A_sub_folder[key_sub_folder[i]] = sub_folder_2
    B_sub_folder[key_sub_folder[i]] = sub_folder_2a


for item in key_sub_folder:
    for item2 in A_sub_folder[item]:
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "1_Stock_Photo" + "\\" + item + "\\" + item2)

print("====================")
count_Length_Folder_Depth = 0
for item in key_sub_folder:
    for item2 in B_sub_folder[item]:
        x = count_Length_Folder_Depth-((Length_Folder_Depth-Length_Folder_Depth_2))
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2)
        
    count_Length_Folder_Depth+=1


print("====================")

for item in key_sub_folder:
    for item2 in A_sub_folder[item]:
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "1_Stock_Photo" + "\\" + item + "\\" + item2 + "\\images")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "1_Stock_Photo" + "\\" + item + "\\" + item2 + "\\labels")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "1_Stock_Photo" + "\\" + item + "\\" + item2 + "\\X_Automate")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "1_Stock_Photo" + "\\" + item + "\\" + item2 + "\\X_Automate\\images")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "1_Stock_Photo" + "\\" + item + "\\" + item2 + "\\X_Automate\\labels")

print("====================")

count_Length_Folder_Depth = 0
for item in key_sub_folder:
    for item2 in B_sub_folder[item]:
        x = count_Length_Folder_Depth-((Length_Folder_Depth-Length_Folder_Depth_2))
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2  + "\\models")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2  + "\\train")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2  + "\\train\\images")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2  + "\\train\\labels")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2  + "\\val")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2  + "\\val\\images")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2  + "\\val\\labels")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2  + "\\test")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2  + "\\test\\images")
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "2_Train_Artefact" + "\\" + key_sub_folder_2[x] + "\\" + item2  + "\\test\\labels")
        
    count_Length_Folder_Depth+=1