import os

# Clear screen command
os.system('cls' if os.name == 'nt' else 'clear')

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\"

print("1. new project")
print("2. load project")

grup = []

lokasi = []
steer = []
box = []
tipe = []

x =100

decision = input("Masukkan Menu : ")
if int(decision) == 1:
    ####################
    print("Buat Project")
    print("")
    ####################
    nama_project = input("Masukkan Nama Project : ")
    print("")

    jumlah_grup = input("Masukkan jumlah lokasi pengambilan gambar : ")
    for i in range(0,int(jumlah_grup)):
        nama_grup = input("masukkan Nama Grup " + str(i+1) + " : ")
        grup.append(nama_grup)

    for i in range(0,len(grup)):
        print(1)





else :
    print("List Project :")