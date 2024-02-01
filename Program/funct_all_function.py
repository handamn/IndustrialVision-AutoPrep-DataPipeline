#this file is basis for all function


file_path = "F:\\repo_generator\\V1\\data_generator\\Project\\RB24\\group.txt"


##### baca_file function
def baca_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]  # Menghapus karakter whitespace dari setiap baris
    return lines

#print(baca_file(file_path))

#print(len(baca_file(file_path)))


tes = baca_file(file_path)


tesss = {}

for i in range(len(tes)):
    key = tes[i]
    value = input("Masukkan Value untuk " + tes[i] + " : ")
    tesss[key] = value

print(tesss)

###############################################