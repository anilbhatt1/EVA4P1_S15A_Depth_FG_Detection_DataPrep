import os
import cv2
import sys

# global vars to inform user whether any of his pictures were not processed well
# don't thank me, I've been through hardship of annoting whole bunch of data then augment to find myself
# with rotten missing dataset...

sucess = 0
fail = 0
X = 224
Y = 224
scaleFactor = 1

new = 'Resized_Scene_Images'
new_path = os.path.join(os.getcwd(),new)

if not os.path.exists(new_path):
    os.makedirs(new_path)
os.chdir(new_path)

def resize(path_to_file):
    for file in os.listdir(path_to_file):
        print (file)
        file_to_read = os.path.join(path_to_file,file)
        img = cv2.imread(file_to_read)
        y,x = img.shape[0],img.shape[1]
        new_name = os.path.basename(os.path.join(path_to_file,file)).split('.')[0]
        file_name = new_name + '_resized.jpg'
        print (file_name)
        while x != 220 or y != 800: 
		x, y = x * scaleFactor, y * scaleFactor
        	x = int(x)
        	y = int(y)
        	resized = cv2.resize(img, (x, y), interpolation=cv2.INTER_AREA)
        	cv2.imwrite(file_name, resized)


resize(r'C:\Users\annbhatt\Desktop\DS_AI\S15A\S15A_Scene Images')