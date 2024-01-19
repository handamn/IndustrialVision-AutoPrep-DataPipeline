import os

# Clear screen command
os.system('cls' if os.name == 'nt' else 'clear')

BASIS_FOLDER = "F:\\repo_generator\\V1\\data_generator\\"

print("1. new project")
print("2. load project")

lokasi = []
steer = []
box = []
tipe = []


decision = input("Masukkan Menu : ")
if int(decision) == 1:
    ####################
    print("Buat Project")
    print("")
    ####################
    nama_project = input("Masukkan Nama Project : ")
    print("")
    #os.mkdir(BASIS_FOLDER + "Project" + "\\" + nama_project)
    ####################
    jumlah_lokasi = input("Masukkan jumlah lokasi pengambilan gambar : ")
    for i in range(0, int(jumlah_lokasi)):
        nama_lokasi = input("Masukkan Nama Lokasi Gambar " + str(i+1) + " : ")
        lokasi.append(nama_lokasi)

        #os.mkdir(BASIS_FOLDER + "Project" + "\\" + nama_project + "\\" + nama_lokasi)
        print("")
    print("")
    
    jumlah_steer = input("Masukkan jumlah posisi steer : ")
    for j in range(0, int(jumlah_steer)):
        nama_steer = input("masukkan Nama Steer " + str(j+1) + " : ")
        steer.append(nama_steer)
        #os.mkdir(BASIS_FOLDER + "Project" + "\\" + nama_project + "\\" + nama_steer)
    print("")

    jumlah_box = input("Masukkan jumlah box : ")
    for k in range(0, int(jumlah_box)):
        nama_box = input("masukkan Nama Box " + str(k+1) + " : ")
        box.append(nama_box)
        print("")
    print("")
    
    jumlah_tipe = input("Masukkan jumlah tipe kendaraan : ")
    for l in range(0, int(jumlah_tipe)):
        nama_tipe = input("masukkan Nama Tipe " + str(l+1) + " : ")
        tipe.append(nama_tipe)
        print("")
    print("")


    print(lokasi)
    print("")
    print(steer)
    print("")
    print(box)
    print("")
    print(tipe)
    print("")


    ####################




    #os.mkdir(BASIS_FOLDER+"Project\\"+nama_folder)
    print("")



else :
    print("List Project :")