import os
import sys

script_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

group = []
sub = []

directory_dict = {}

project_location = "\\Project"


Name_Project = str(input("Enter Name Project : "))
Folder_Depth = int(input("Enter Folder Depth : "))

for i in range(Folder_Depth - 1):
    Name_Group = str(input("Enter Grouping Name for depth " + str(i+1) + " : "))
    group.append(Name_Group)
    
    count_subfolder = int(input("Enter How Much Subfolder for " + Name_Group + " : "))
    
    sub.append([])

    di = []

    for j in range (count_subfolder):
        Name_Sub = str(input("Enter Sub Name for " + Name_Group + " Sub " + str(j+1) + " : "))
        sub[i].append(Name_Sub)

        di.append(Name_Sub)
    
    directory_dict[Name_Group] = di

print(sub)
    
    
print("")

print(directory_dict)