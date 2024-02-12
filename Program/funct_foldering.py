import os
import sys

##############################
def print_combinations(value_list, current_combination=[]):
    if not value_list:
        # Base case: If value_list is empty, print the current combination
        #print("\\".join(current_combination))
        print(script_directory + project_location + "\\" + Name_Project + "\\" + "\\".join(current_combination))
        #return script_directory + project_location + "\\" + Name_Project + "\\" + "\\".join(current_combination)
    
    else:
        # Recursive case: Iterate through each item in the current list and call the function recursively
        for item in value_list[0]:
            print_combinations(value_list[1:], current_combination + [item])



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
tes = []

for i in range(len(value_list)):
    if i+1 == len(value_list):
        print("masuk disini")
        print("")
        Create_Dir_list.append(value_list[i])
        print_combinations(Create_Dir_list)
        print("")

    else:
        print("")
        Create_Dir_list.append(value_list[i])
        print_combinations(Create_Dir_list)
        print("")

print(len(value_list))
print(Create_Dir_list[-1])
print("===============")
print("")
print("===============")

def generate_combinations2(value_list, current_combination=[]):
    if not value_list:
        # Base case: If value_list is empty, return the current combination
        return "\\".join(current_combination)
    else:
        combinations = []
        # Recursive case: Iterate through each item in the current list and call the function recursively
        for item in value_list[0]:
            combinations.append(generate_combinations2(value_list[1:], current_combination + [item]))
        return combinations

combinations2 = generate_combinations2(value_list)

# Print the combinations
for combination in combinations2:
    print(combination)

print("===============")
print("")
print("===============")

print(len(combinations2))
print(combinations2)
print(type(combinations2))

print("===============")
print("")
print("===============")

print(value_list)

"""
for i in range(len(combinations2)):
    for j in range(len(combinations2[i])):
        for k in range(len(combinations2[i][j])):
            print(combinations2[i][j][k])

"""



def display_list_recursive(lst):
    if isinstance(lst, list):
        for item in lst:
            display_list_recursive(item)
    else:
        print(lst)

print("")
display_list_recursive(combinations2)

