import os
import time
from datetime import datetime
import cv2
import random
import shutil
import yaml
import subprocess
import torch
import pandas as pd
from tqdm import tqdm
import csv

#from pathlib import path
#from models.experimental import attempt_load
#from utils.general import non_max_suppression

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


def repeat():
    get_input = str(input("Finish Process ? (yes/no) : "))
    
    if (get_input == "yes"):
        condition = True
        return condition
    
    else:
        condition = False
        return condition


def baca_file(route):
    all_data = {}
    before_data = {}
    after_data = {}

    empty_found = False

    with open(route, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if not stripped_line:  # Cek apakah baris kosong
                empty_found = True
                continue  # Loncat ke baris berikutnya

            key, values = stripped_line.split(': ')
            value_list = values.split(' ')
            all_data[key] = value_list
            
            if empty_found:
                after_data[key] = value_list
            else:
                before_data[key] = value_list

    key_list = list(all_data.keys())
    value_list = list(all_data.values())
    before_key = list(before_data.keys())
    before_value = list(before_data.values())
    after_key = list(after_data.keys())
    after_value = list(after_data.values())

    return key_list, value_list, before_key, before_value, after_key, after_value
    


def data_input_default(route, decision):
    key_list, value_list, before_key, before_value, after_key, after_value = baca_file(route)
    dict_value_input = {}

    for i in range(len(key_list)):
        value = input("Enter Value for " + key_list[i] + "            : ")
        dict_value_input[i] = value
    return dict_value_input


def data_train_input():
    epochs_count  = input("Enter How Many Epochs     (ex : 100)             : ")
    model_type    = input("Enter Train Model Conf    (ex : yolov5l_CBAM_2)  : ")
    batch_count   = input("Enter Batch Count         (ex : -1)              : ")
    pat_count     = input("Enter Patience            (ex : 100)             : ")

    return epochs_count, model_type, batch_count, pat_count


def simple_route(main_route, decision):
    if decision == "complete":
        group_route = main_route + "group.txt"
    else :
        group_route = main_route + "group_crop.txt"

    base_route = main_route + "1_Stock_Photo"

    list_of_input = data_input_default(group_route, "key")

    for i in range(len(list_of_input)):
        base_route += "\\" + list_of_input[i]

        if i == len(list_of_input)-1:
            code = list_of_input[i]
    
    automate_route = base_route + "\\X_Automate"

    return base_route, automate_route, code


def read_csv(file_name):
    try:
        with open(file_name, 'r', newline='') as file_csv:
            reader = csv.reader(file_csv)
            data = [row[0] for row in reader]  # Ambil hanya kolom pertama dari setiap baris
            return sorted(data)  # Mengurutkan data
    except FileNotFoundError:
        return []


def write_csv(file_name, data):
    with open(file_name, 'w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        for item in data:
            writer.writerow([item])


def add_data(data, input_string):
    data.append(input_string)
    return sorted(data)


def capture(route_path, decision):
    base_route, automate_route, code = simple_route(route_path, decision)
    image_count = int(input("Enter How Many Image      (ex : 100)             : "))

    image_route = base_route + "\\images" 
    cap = cv2.VideoCapture(5)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

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


def pick_rand(route_path, decision):
    base_route, automate_route, code = simple_route(route_path, decision)

    image_count = int(input("Enter How Many Image      (ex : 100)             : "))

    image_source_route = base_route + "\\images"
    sub_automate_image_route = automate_route + "\\images"
    sub_automate_labels_route = automate_route + "\\labels"
    txt_route = sub_automate_labels_route + "\\classes.txt"
    yaml_route = automate_route + "\\" + code + ".yaml"

    with open(txt_route, 'w') as file:
        file.write(code)

    copy_random_images(image_source_route, sub_automate_image_route, image_count)

    data = {
        'train' : automate_route,
        'val' : automate_route,
        'names' : {0: code}
    }

    with open(yaml_route, 'w') as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

    print("FINISH")


def labeling(route_path, decision):
    base_route, automate_route, code = simple_route(route_path, decision)
    image_route = automate_route + "\\images"
    label_route = automate_route + "\\labels\\classes.txt"

    command = ["labelimg",
                image_route,
                label_route]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()


def train(folder_route, program_route, decision):
    if decision == "Begin":
        group_route = folder_route + "group.txt"
        base_route = folder_route + "1_Stock_Photo"
    
    else :
        group_route = folder_route + "group_crop.txt"
        base_route = folder_route + "2_Train_Artefact"

    list_of_input = data_input_default(group_route, "key")
    epochs_count, model_type, batch_count, pat_count = data_train_input()

    for i in range(len(list_of_input)):
        base_route += "\\" + list_of_input[i]

        if i == len(list_of_input)-1:
            code = list_of_input[i]

    if decision == "Begin":
        automate_route = base_route + "\\X_Automate"
    
    else :
        automate_route = base_route
    
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
                "--batch-size", batch_size_source,
                "--patience", patience_size_source,
                "--imgs", str(320)]

    run_python_file(train_file, argument)


def Auto_Anotate(route_path, program_route, decision):
    base_route, automate_route, code = simple_route(route_path, decision)
    
    model_type = str(input("Enter Model Train              (ex : train1)  : "))

    folder_train_images = base_route + "\\images"
    folder_train_labels = base_route + "\\labels"
    folder_model = base_route + "\\Models\\" + model_type + "\\weights\\best.pt"
    yolo_route = program_route + "\\yolov5"
    model = torch.hub.load(yolo_route, "custom", path=folder_model, source = "local", force_reload = True)

    train_list = os.listdir(folder_train_images)
    
    for name in tqdm(train_list, desc= "Processing Images"):
        label_name = f"{name.split('.')[0]}.txt"
        label_directory = os.path.join(folder_train_labels, label_name)

        image_directory = os.path.join(folder_train_images, name)
        results = model(image_directory)
        xyxy_results = results.pandas().xyxy[0]

        if not xyxy_results.empty:
            xmin = xyxy_results['xmin'][0]
            ymin = xyxy_results['ymin'][0]
            xmax = xyxy_results['xmax'][0]
            ymax = xyxy_results['ymax'][0]
            group = xyxy_results['class'][0]

            index_class = 0

            xcenter = ((xmax+xmin)/2)/640
            ycenter = ((ymax+ymin)/2)/480
            width = (xmax-xmin)/640
            height = (ymax-ymin)/480

            text = str(index_class) + " " + str(xcenter) + " " + str(ycenter) + " " + str(width) + " " + str(height)

            with open(label_directory, "w") as f:
                f.write(text)
        
        words = base_route.split('\\')
        code_type = words[-1]

    with open(f"{folder_train_labels}/classes.txt", "w") as f:
        f.write(code_type)
    
    folder_csv = base_route + "\\class_index.csv"

    if not os.path.exists(folder_csv):
        with open(folder_csv, "w", newline=""):
            pass

    data = read_csv(folder_csv)
    data = add_data(data, code_type)
    write_csv(folder_csv, data)

def run_python_file(file_name, arguments=None):
    try:
        subprocess.run(["python", file_name] + (arguments or []), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")