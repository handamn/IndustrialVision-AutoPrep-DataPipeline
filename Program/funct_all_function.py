import os
import time
from datetime import datetime
import cv2
import random
import shutil
import yaml
import subprocess

def print_menu():
    print("\nProgram Generator\n")
    print("Pilih Menu :")
    print("1. Ambil Gambar")
    print("2. Pilih Random 50")
    print("3. Anotasi")
    print("4. Training Prepare Image")
    print("5. Auto Anotasi")
    print("6. Combine")
    print("7. Training Final\n")

    hasil_menu    = input("Enter Menu                                       : ")
    # Clear screen command
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================================")
    return hasil_menu


def baca_file(route):
    with open(route, 'r') as file:
        lines = [line.strip() for line in file.readlines()]  # Menghapus karakter whitespace dari setiap baris
    return lines


def data_input_default(route):
    list_var = baca_file(route)
    dict_value_input = {}

    for i in range(len(list_var)):
        value = input("Masukkan Value untuk " + list_var[i] + " : ")
        dict_value_input[i] = value
    return dict_value_input



def capture(route_path):
    group_route = route_path + "group.txt"
    image_route = route_path + "1_Stock_Photo"

    list_of_input = data_input_default(group_route)
    image_count = int(input("Enter How Many Image      (ex : 100)             : "))

    for i in range(len(list_of_input)):
        image_route += "\\" + list_of_input[i]

    image_route += "\\images" 

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


def copy_random_images(source_folder, destination_folder, num_images):
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    num_images = min(num_images, len(image_files))
    random_images = random.sample(image_files, num_images)

    for image in random_images:
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(destination_folder, image)
        shutil.copy2(source_path, destination_path)
        print(f"Copied: {image}")


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
    automate_route = image_route + "\\X_Automate"
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


def labeling(route_path):
    group_route = route_path + "group.txt"
    base_route = route_path + "1_Stock_Photo"

    list_of_input = data_input_default(group_route)

    for i in range(len(list_of_input)):
        base_route += "\\" +list_of_input[i]

        if i == len(list_of_input)-1:
            code = list_of_input[i]
    
    automate_route = base_route + "\\X_Automate"
    image_route = automate_route + "\\images"
    label_route = automate_route + "\\labels\\classes.txt"

    command = ["labelimg",
                image_route,
                label_route]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()


def data_train_input():
    epochs_count  = input("Enter How Many Epochs     (ex : 100)             : ")
    model_type    = input("Enter Train Model Conf    (ex : yolov5l_CBAM_2)  : ")
    batch_count   = input("Enter Batch Count         (ex : -1)              : ")
    pat_count     = input("Enter Patience            (ex : 100)             : ")

    return epochs_count, model_type, batch_count, pat_count

def train(folder_route, program_route):
    group_route = folder_route + "group.txt"
    base_route = folder_route + "1_Stock_Photo"

    list_of_input = data_input_default(group_route)
    epochs_count, model_type, batch_count, pat_count = data_train_input()

    for i in range(len(list_of_input)):
        base_route += "\\" + list_of_input[i]

        if i == len(list_of_input)-1:
            code = list_of_input[i]
    
    automate_route = base_route + "\\X_Automate"
    yaml_route = automate_route + "\\" + code + ".yaml"
    project_source = automate_route + "\\Models"
    epochs_source = epochs_count
    cfg_source = program_route + "\\models\\" + model_type + ".yaml"
    batch_size_source = batch_count
    patience_size_source = pat_count
    train_file = program_route + "\\yolov5\\train.py"

    argument = ["--data", yaml_route,
                "--project", project_source,
                "--epochs", epochs_source,
                "--weights", "",
                "--cfg", cfg_source,
                "--batch_size", batch_size_source,
                "--patience", patience_size_source]

    run_python_file(train_file, argument)