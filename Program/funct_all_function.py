#this file is basis for all function

##### Function for input default item
def data_input_default():
    car           = input("Enter Car Model           (ex : Innova)          : ")
    steer         = input("Enter Steer               (ex : RHD)             : ")
    box           = input("Enter Box Class           (ex : Box1)            : ")
    kode_box      = input("Enter Code Box            (ex : X_3_CDE)         : ")
    kendaraan = car + "_" + steer

    return kendaraan, box, kode_box
#################################################