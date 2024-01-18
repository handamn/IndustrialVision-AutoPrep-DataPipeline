import os
import random
import shutil
import yaml
import subprocess

# Clear screen command
os.system('cls' if os.name == 'nt' else 'clear')

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\"

print("1. new project")
print("2. load project")

decision = input("masukkan : ")
if int(decision) == 1:
    print("Buat projek")
    nama_folder = input("masukkan nama project : ")
    os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder)

    count_subfolder = input("Masukkan berapa subfolder (in/out) : ")
    for x in range(0,int(count_subfolder)):
        nama_folder_x = input("Masukkan Nama Folder X ")
        item_subfolder = input("Berapa banyak item subfolder : ")
        os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder+"\\"+nama_folder_x+"\\")
        for i in range(0,int(item_subfolder)):
            nama_subfolder = input("masukkan nama subfoldernya ")
            os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder+"\\"+nama_folder_x+"\\"+nama_subfolder+"\\")
            os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder+"\\"+nama_folder_x+"\\"+nama_subfolder+"\\"+"images"+"\\")
            os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder+"\\"+nama_folder_x+"\\"+nama_subfolder+"\\"+"labels"+"\\")
            os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder+"\\"+nama_folder_x+"\\"+nama_subfolder+"\\"+"X_Automasi"+"\\")
            os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder+"\\"+nama_folder_x+"\\"+nama_subfolder+"\\"+"X_Automasi"+"\\"+"images"+"\\")
            os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder+"\\"+nama_folder_x+"\\"+nama_subfolder+"\\"+"X_Automasi"+"\\"+"labels"+"\\")
            os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder+"\\"+nama_folder_x+"\\"+nama_subfolder+"\\"+"models"+"\\")
            i+=1
        x+=1

else :
    print("list project")
    print()
    dir_list = os.listdir("F:\\repo_generator\\V1\\data_generator\\Project")
    x = 1
    for i in dir_list:
        print(str(x)+" "+str(i))
        x+=1

    masukan = input("coba entry index")
    print(dir_list[int(masukan)-1])
    
    