#this file is basis for all function
import cv2
import os
import time
from datetime import datetime
import cv2



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
def capture(route_path):

    group_route = route_path + "group.txt"
    image_route = route_path + "1_Stock_Photo"

    list_of_input = read.data_input_default(group_route)
    image_count = int(input("Enter How Many Image      (ex : 100)             : "))

    for i in range(len(list_of_input)):
        image_route += "\\" + list_of_input[i]

    image_route += "\\imag es" 

    cap = cv2.VideoCapture(0)

        # Looping image save program
    for imgnum in range(image_count):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]

        imgname = os.path.join(image_route, f'{timestamp}.jpg')
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
    print(image_route)
    print("")
    print("======================================================================================================")
############################ End of Collections