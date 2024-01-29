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
        print("")
        for j in range(0, int(jumlah_steer)):
            nama_steer = input("masukkan Nama Steer " + str(j+1) + ", " + nama_lokasi +" : ")
            print("")
            for k in range(0, int(jumlah_box)):
                print("")
                nama_box = input("masukkan Nama Box " + str(k+1) + ", " + nama_lokasi + ", " + nama_steer + " : ")
                for l in range(0, int(jumlah_tipe)):
                    print("")
                    nama_tipe = input("Masukkan Nama Tipe " + str(l+1) +  ", " + nama_lokasi + ", " + nama_steer + ", " + nama_box + " : ")
                    #os.makedirs(BASIS_FOLDER + "Project" + "\\" + nama_project + "\\" + nama_lokasi)
                    #os.makedirs(BASIS_FOLDER + "Project" + "\\" + nama_project + "\\" + nama_lokasi + "\\" + nama_steer)
                    #os.makedirs(BASIS_FOLDER + "Project" + "\\" + nama_project + "\\" + nama_lokasi + "\\" + nama_steer + "\\" + nama_box)
                    os.makedirs(BASIS_FOLDER + "Project" + "\\" + nama_project + "\\" + nama_lokasi + "\\" + nama_steer + "\\" + nama_box + "\\" + nama_tipe)

    ####################



else :
    print("List Project :")