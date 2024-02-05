#this file is basis for all function
import cv2
import os
import time
from datetime import datetime
import cv2
import subprocess



file_path = "F:\\repo_generator\\V1\\data_generator\\Project\\RB24\\group.txt"

##### baca_file function
def baca_file(route):
    with open(route, 'r') as file:
        lines = [line.strip() for line in file.readlines()]  # Menghapus karakter whitespace dari setiap baris
    return lines
###############################################

##### Function for input default item
def data_input_default(route):
    list_var = baca_file(route)
    dict_value_input = {}

    for i in range(len(list_var)):
        value = input("Masukkan Value untuk " + list_var[i] + " : ")
        dict_value_input[i] = value

    return dict_value_input

###############################################

##### ##### collections of cameras function
fe_path = "F:\\repo_generator\\V1\\data_generator\\Project\\RB24\\group.txt"
list_of_input = read.data_input_default(fe_path)

jumlah_gambar = int(input("Enter How Many Image      (ex : 100)             : "))

basis_folder = "F:\\repo_generator\\V1\\data_generator\\Project\\RB24\\1_Stock_Photo"

simpan_folder = basis_folder

for i in range(len(list_of_input)):
    simpan_folder += "\\" + list_of_input[i]

simpan_folder += "\\images"

number_images = jumlah_gambar

cap = cv2.VideoCapture(0)

# Looping image save program
for imgnum in range(number_images):
    print('Collecting image {}'.format(imgnum))
    ret, frame = cap.read()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]

    imgname = os.path.join(simpan_folder, f'{timestamp}.jpg')
    cv2.imwrite(imgname,frame)
    cv2.imshow('frame',frame)
    time.sleep(0.0001)

    if cv2.waitKey(1)&0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("")
print("======================================================================================================")
print("")
print("----------------------------------------AMBIL GAMBAR BERHASIL-----------------------------------------")
print("")
print("------------------------------------------Gambar disimpan di------------------------------------------")
print("")
print(simpan_folder)
print("")
print("======================================================================================================")
############################ End of Collections


##### pick_rand funtion
def pick_rand(route_path):
    group_route = route_path + "group.txt"
    image_route = route_path + "1_Stock_Photo"

    list_of_input = data_input_default(group_route)
    image_count = int(input("Enter How Many Image      (ex : 100)             : "))

    for i in range(len(list_of_input)):
        image_route += "\\" + list_of_input[i]

        if i == len(list_of_input)-1:
            code = list_of_input[i]

    
    source_route = image_route + "\\images"
    automate_route = image_route + "\\X_Automasi"
    sub_automate_image_route = automate_route + "\\images"
    sub_automate_labels_route = automate_route + "\\labels"
    txt_route = sub_automate_labels_route + "\\classes.txt"
    yaml_route = automate_route + "\\" + code + ".yaml"

    with open(txt_route, 'w') as file:
        file.write(code)

    copy_random_images(source_route, sub_automate_image_route, image_count)


    data = {
        'train' : automate_route,
        'val' : automate_route,
        'names' : {0: code}
    }

    with open(yaml_route, 'w') as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

    print("FINISH")

###############################################


##### labeling function
subprocess.run("labelimg")
###############################################