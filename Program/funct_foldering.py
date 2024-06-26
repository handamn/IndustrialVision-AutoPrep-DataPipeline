import os
import sys
import csv

##############################
def Create_Dir_Base(base, branch, value_list, current_combination=[]):
    if not value_list:
        path_create = base + branch + "\\" + "\\".join(current_combination)
        os.mkdir(path_create)

    else:
        for item in value_list[0]:
            Create_Dir_Base(base, branch, value_list[1:], current_combination + [item])


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


def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list


def write_text(link_path, list_data, name_file):
    file_name = link_path + "\\" + name_file + ".txt"
    with open(file_name, 'w') as file:
        for key, value in list_data.items():
            if key is None or value is None:
                file.write("\n")
            else:
                file.write(f"{key}: {' '.join(value)}\n")


def create_folder(source_path, list_value, subject_folder):
    Create_Dir_list_3 = []
    for i in range(len(list_value)):
        if i+1 == len(list_value):
            Create_Dir_list_3.append(list_value[i])
            Create_Dir_Base(source_path, subject_folder, Create_Dir_list_3)
        
        else :
            Create_Dir_list_3.append(list_value[i])
            Create_Dir_Base(source_path, subject_folder, Create_Dir_list_3)


def length_measure(list_value):
    length_count = 1
    for i in range(len(list_value)):
        length_count *= len(list_value[i])
    return length_count


def list_to_csv(data_list, file_name):
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for item in data_list:
            writer.writerow([item])

##############################

def master_program(base_folder):
    Name_Project = str(input("Enter Name Project : "))
    Folder_Depth = int(input("Enter Folder Depth : "))

    final_path = base_folder + "\\" + Name_Project + "\\"
    st_path = final_path + "1_Stock_Photo\\"
    nd_path = final_path + "2_Train_Artefact\\"

    os.mkdir(final_path)
    os.mkdir(st_path)
    os.mkdir(nd_path)

    directory_dict = {}

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

    Last_Name_Group = str(input("Enter Grouping Name for depth " + str(Folder_Depth) + " : "))
    key_list.append(Last_Name_Group)

    directory_dict[Last_Name_Group] = "BLANK"
    write_text(final_path, directory_dict, "group")

    potong = str(input("Group Tier to Combine : "))
    ind = int(key_list.index(potong))
    poto = ind+1
    new_value_list = value_list[ind+1:]
    new_key_list = key_list[ind+1:]

    before_directory_dict_conversion = list(directory_dict.keys())
    before_directory_dict = {before_directory_dict_conversion[i]:directory_dict[before_directory_dict_conversion[i]] for i in range(ind+1)}

    before_directory_dict[None] = None

    after_directory_dict_conversion = list(directory_dict.items())
    after_directory_dict_conversion.pop(ind)
    after_directory_dict = dict(after_directory_dict_conversion)

    write_directory_dict = before_directory_dict
    write_directory_dict.update(after_directory_dict)

    write_text(final_path, write_directory_dict, "group")


    new_key_list = key_list[ind+1:]
    conversion = list(directory_dict.items())
    conversion.pop(ind)
    new_directory_dict = dict(conversion)

    write_text(final_path, new_directory_dict, "group_crop")

    Length_Folder_Depth = length_measure(value_list)
    Length_Folder_Depth_2 = length_measure(new_value_list)    

    create_folder(final_path, value_list, "1_Stock_Photo")
    Storing_Group_Name = Store_Dir_Base(value_list)

    create_folder(final_path, new_value_list, "2_Train_Artefact")
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
            Name_Sub_2 = str(input("Enter Sub Name for " + key_sub_folder[i] + " -" + str(j+1) + "- : "))
            sub_folder_2.append(Name_Sub_2)

            if (i+1) > (Length_Folder_Depth-Length_Folder_Depth_2):
                sub_folder_2a.append(Name_Sub_2)
        
        A_sub_folder[key_sub_folder[i]] = sub_folder_2
        B_sub_folder[key_sub_folder[i]] = sub_folder_2a


    store_csv = {}

    for item in key_sub_folder:
        for item2 in A_sub_folder[item]:
            os.mkdir(st_path + item + "\\" + item2)
            os.mkdir(st_path + item + "\\" + item2 + "\\images")
            os.mkdir(st_path + item + "\\" + item2 + "\\labels")
            os.mkdir(st_path + item + "\\" + item2 + "\\models")
            os.mkdir(st_path + item + "\\" + item2 + "\\X_Automate")
            os.mkdir(st_path + item + "\\" + item2 + "\\X_Automate\\images")
            os.mkdir(st_path + "\\" + item + "\\" + item2 + "\\X_Automate\\labels")

            words = item.split('\\')
            code_type = words[:1]
            code2 = ""
            first_group = code2.join(code_type)

            index_type = words[1:]
            code0 = "\\"
            index_store = code0.join(index_type)


            if (directory_dict[key_list[0]][0]) == first_group :
                store_csv[index_store] = A_sub_folder[item]
                list_to_csv(A_sub_folder[item], (st_path + item + "\\" + "index_class.csv"))
            

            else :
                list_to_csv(store_csv[index_store], (st_path + item + "\\" + "index_class.csv"))




    count_Length_Folder_Depth = 0
    for item in key_sub_folder:
        for item2 in B_sub_folder[item]:
            x = count_Length_Folder_Depth-((Length_Folder_Depth-Length_Folder_Depth_2))
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2)
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2  + "\\models")
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2  + "\\train")
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2  + "\\train\\images")
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2  + "\\train\\labels")
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2  + "\\val")
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2  + "\\val\\images")
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2  + "\\val\\labels")
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2  + "\\test")
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2  + "\\test\\images")
            os.mkdir(nd_path + key_sub_folder_2[x] + "\\" + item2  + "\\test\\labels")
            
        count_Length_Folder_Depth+=1

