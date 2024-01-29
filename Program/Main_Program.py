import os

# Clear screen command
os.system('cls' if os.name == 'nt' else 'clear')

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\"

print("1. new project")
print("2. load project")


decision = input("Masukkan Menu : ")
if int(decision) == 1:
    ####################
    print("Buat Project")
    print("")
    ####################
    nama_project = input("Masukkan Nama Project : ")
    print("")
    os.mkdir(BASIS_FOLDER + "Project" + "\\" + nama_project)
    ####################
    jumlah_lokasi = input("Masukkan jumlah lokasi pengambilan gambar : ")
    print("")
    jumlah_steer = input("Masukkan jumlah posisi steer : ")
    print("")
    jumlah_box = input("Masukkan jumlah box : ")
    print("")
    jumlah_tipe = input("Masukkan jumlah tipe kendaraan : ")
    print("")
    for i in range(0, int(jumlah_lokasi)):
        nama_lokasi = input("Masukkan Nama Lokasi Gambar " + str(i+1) + " : ")
        os.mkdir(BASIS_FOLDER + "Project" + "\\" + nama_project + "\\" + nama_lokasi)
        print("")

    for j in range(0, int(jumlah_steer)):
        nama_steer = input("masukkan Nama Steer " + str(j+1) + " : ")
        os.mkdir(BASIS_FOLDER + "Project" + "\\" + nama_project + "\\" + nama_steer)



    ####################




    #os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder)
    print("")



else :
    print("List Project :")