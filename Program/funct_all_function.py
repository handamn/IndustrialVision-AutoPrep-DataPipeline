import csv

def baca_file(route, decision):
    data = {}
    with open(route, 'r') as file:
        for line in file:
            key, values = line.strip().split(': ')
            data[key] = values.split(' ')

    key_list = list(data.keys())
    value_list = list(data.values())
    
    if decision == "key":
        return key_list
    
    else:
        return value_list[decision]


def baca_file2(route, decision):
    data = {}
    with open(route, 'r') as file:
        for line in file:
            key, values = line.strip().split(': ')
            data[key] = values.split(' ')

    key_list = list(data.keys())
    value_list = list(data.values())

    return key_list, value_list


def data_input_default(route, decision):
    list_var = baca_file(route, decision)
    dict_value_input = {}

    for i in range(len(list_var)):
        value = input("Masukkan Value untuk " + list_var[i] + " : ")
        dict_value_input[i] = value
    return dict_value_input



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

    return base_route, automate_route


def data_input_default2(route, decision):
    base = route + "group.txt"
    base2 = route + "group_crop.txt"

    list_var, val_var = baca_file2(base, decision)
    list_var_crop, val_crop = baca_file2(base2, decision)

    dict_value_input = {}
    dict_value_input_crop = {}

    for i in range(len(list_var)):
        value = input("Masukkan Value untuk " + list_var[i] + " : ")
        dict_value_input[i] = value

        for j in range(len(list_var_crop)):
            if list_var[i] == list_var_crop[j]:
                dict_value_input_crop[j] = value
    
    return dict_value_input, dict_value_input_crop


def simple_route2(main_route):
    og_base_route = main_route + "1_Stock_Photo"
    og_list_of_input, crop_list_of_input = data_input_default2(main_route, "key")

    input_result_route = ""
    mod_input_result_route = ""

    for i in range(len(og_list_of_input)):
        og_base_route += "\\" + og_list_of_input[i]
        input_result_route += og_list_of_input[i] + "\\"

        if i == len(og_list_of_input)-1:
            code = og_list_of_input[i]

    og_automate_route = og_base_route + "\\X_Automate"

    for i in range(len(crop_list_of_input)):
        if i < (len(crop_list_of_input)-1):
            mod_input_result_route += crop_list_of_input[i] + "\\"


    return og_base_route, og_automate_route, code, input_result_route, mod_input_result_route

def csv_file_reader(nama_file):
    data = []
    with open(nama_file, 'r') as file_csv:
        reader = csv.reader(file_csv)
        for baris in reader:
            data.append(baris[0])  # Ambil elemen pertama dari setiap baris
    return data

def split_data_main():
    print("hehehe")

def split_data(route_path, decision):
    base_route, automate_route = simple_route(route_path, decision)

    print("")
    print(base_route)
    print(automate_route)
    print("")

    parse_base_route = base_route.split("\\")
    parse_base_route_class = parse_base_route[:-1]
    index_class_route = "\\".join(parse_base_route_class)

    class_file = index_class_route + "\\index_class.csv"
    data_csv = csv_file_reader(class_file)
    output = route_path + "2_Train_Artefact"

    get_code = parse_base_route[-1]
    
    for code in data_csv:
        print(code)
        print(index_class_route + "\\" + code)


def coba(route_path, decision):
    base_route, automate_route = simple_route(route_path, decision)

    print(base_route)
    if base_route.startswith(route_path+"1_Stock_Photo\\"):
        value_input = base_route[len(route_path+"1_Stock_Photo\\"):]

    print(value_input)
    print("============")
    print("")

def coba2(route_path):
    base_route, automate_route, code, input_result_route, mod_input_result_route = simple_route2(route_path)

    parse_base_route = base_route.split("\\")
    parse_base_route_class = parse_base_route[:-1]
    index_class_route = "\\".join(parse_base_route_class)

    class_file = index_class_route + "\\index_class.csv"
    data_csv = csv_file_reader(class_file)
    output = route_path + "2_Train_Artefact"

    print("")
    print(route_path)
    print("")
    print(base_route)
    print("")
    print(automate_route)
    print("")
    print(code)
    print("")
    print(input_result_route)
    print("")
    print(mod_input_result_route)


coba2("F:\\repo_generator\\V1\\data_generator\\Project\\RB1\\")
