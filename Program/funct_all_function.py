#this file is basis for all function


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
