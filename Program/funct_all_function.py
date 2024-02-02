#this file is basis for all function
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
##### listing active camera
def list_active_cameras(max_cameras=10):
    active_cameras = []
    for index in range(max_cameras):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            active_cameras.append(index)
            cap.release()
    return active_cameras
###############################################

##### Displaying the camera
def display_cameras(cameras):
    caps = [cv2.VideoCapture(i) for i in cameras]
    
    while True:
        for i, cap in enumerate(caps):
            ret, frame = cap.read()
            if ret:
                cv2.imshow(f'Camera {cameras[i]}', frame)
            else:
                print(f"Failed to get frame from Camera {cameras[i]}")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for cap in caps:
        cap.release()
    cv2.destroyAllWindows()
###############################################

active_cameras = list_active_cameras()

# Print active cameras
if active_cameras:
    print(f"Active cameras found at indices: {active_cameras}")
    display_cameras(active_cameras)
else:
    print("No active cameras found.")
    
############################ End of Collections