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

    print(base_route)
    print(automate_route)
    print("")

    parse_base_route = base_route.split("\\")
    parse_base_route_class = parse_base_route[:-1]
    index_class_route = "\\".join(parse_base_route_class)

    class_file = index_class_route + "\\index_class.csv"
    data_csv = csv_file_reader(class_file)
    output = route_path + "2_Train_Artefact"

    print(class_file)
    print(output)

    """if main_code in data_csv:
        for code in data_csv:
            if code != """



#split_data("F:\\repo_generator\\V1\\data_generator\\Project\\RB13\\", "complete")
#print("")
split_data("F:\\repo_generator\\V1\\data_generator\\Project\\RB1\\", "complete")

"""
F:\repo_generator\V1\data_generator\Project\RB8\1_Stock_Photo\Laboratory\LHD\Box1\X_1_A
F:\repo_generator\V1\data_generator\Project\RB8\1_Stock_Photo\Laboratory\LHD\Box1\X_1_A\X_Automate
"""